from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
import random
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "users.json")
os.makedirs("data", exist_ok=True)

users_data = {}
current_user = None  # Will store the logged-in username

# ✅ Load existing users if file exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        try:
            users_data = json.load(f)
        except json.JSONDecodeError:
            print("[WARN] Could not load users.json, starting fresh.")
            users_data = {}

# ✅ Save all users to file
def save_all_users():
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(users_data, f, indent=4)
        print("[DEBUG] All users saved successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to save users: {e}")

# ✅ Save current user data
def save_user_data():
    global current_user, user_data  # ← add user_data here too
    if current_user and current_user in users_data:
        users_data[current_user] = user_data
        save_all_users()
    else:
        print("[ERROR] No user is currently logged in.")






# Function to calculate BMI and recommendations
def calculate_recommendations():
    global current_user
    if not current_user or current_user not in users_data:
        print("[ERROR] No current user selected or user not found.")
        return 0, "unknown", 0, 0.0, "unknown"

    user_data = users_data[current_user]  # 👈 Get current user's data

    # Convert to metric if needed
    height_cm = user_data['height_value'] * 2.54 if user_data['height_unit'] == 'inch' else user_data['height_value']
    weight_kg = user_data['weight_value'] * 0.453592 if user_data['weight_unit'] == 'lb' else user_data['weight_value']
    height_m = height_cm / 100

    bmi = round(weight_kg / (height_m ** 2), 2)

    # Determine goal
    goal = "fit"
    if bmi < 18.5:
        goal = "gain weight"
    elif bmi > 25:
        goal = "lose weight"

    # BMR & Recommendations
    sex = user_data['sex']
    age = user_data['age']
    activity_factor = 1.55
    if age < 18:
        activity_factor = 1.3
    elif age > 50:
        activity_factor = 1.4

    if sex == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    daily_calories = int(bmr * activity_factor)
    water_liters = round(weight_kg * 0.035, 1)
    sleep_hours = "8–10 hours" if age < 18 else "7–9 hours"

    return bmi, goal, daily_calories, water_liters, sleep_hours
exercise_presets = {
    "Push-ups": ("Push-ups", "20 reps"),
    "Plank": ("Plank", "60 seconds"),
    "Jumping Jacks": ("Jumping Jacks", "30 reps"),
    "Squats": ("Squats", "20 reps"),
    "Lunges": ("Lunges", "15 each leg"),
    "Sit-ups": ("Sit-ups", "25 reps"),
    "Burpees": ("Burpees", "15 reps"),
    "Run": ("Run", "2 km")
}


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.username = TextInput(hint_text="Username")
        self.password = TextInput(hint_text="Password (optional)", password=True)  # Can be extended later
        login_btn = Button(text="Login")
        signup_btn = Button(text="Sign Up")
        login_btn.bind(on_press=self.login)
        signup_btn.bind(on_press=self.signup)

        layout.add_widget(Label(text="Welcome to Be a Man!"))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)
        layout.add_widget(signup_btn)
        self.add_widget(layout)

    def login(self, instance):
        global current_user
        user = self.username.text.strip()

        if user in users_data:
            current_user = user
            print(f"[DEBUG] Logged in as: {user}")
            self.manager.current = 'title'
        else:
            print("[ERROR] User not found.")

    def signup(self, instance):
        global current_user  # ✅ Fixed indentation here
        user = self.username.text.strip()
        if user not in users_data:
            users_data[user] = {
                "name": user,
                "age": 0,
                "sex": "",
                "height_value": 0,
                "height_unit": "cm",
                "weight_value": 0,
                "weight_unit": "kg",
                "workout_days": [],
                "plan_progress": {}
            }
            save_all_users()
            current_user = user
            print(f"[DEBUG] New user created: {user}")
            self.manager.current = 'title'
        else:
            print("[ERROR] User already exists.")





class TitleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        title_label = Label(text="🔥 Be a Man 🔥", font_size=40)
        start_btn = Button(text="Start", size_hint=(1, 0.2), font_size=24)
        start_btn.bind(on_press=self.go_next)

        layout.add_widget(title_label)
        layout.add_widget(start_btn)
        self.add_widget(layout)

    def go_next(self, instance):
        self.manager.current = 'input'


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.name_input = TextInput(hint_text="Name")
        self.age_input = TextInput(hint_text="Age", input_filter='int')

        self.sex_label = Label(text="Sex")
        sex_box = BoxLayout()
        self.male = ToggleButton(text="Male", group='sex')
        self.female = ToggleButton(text="Female", group='sex')
        sex_box.add_widget(self.male)
        sex_box.add_widget(self.female)

        self.height_input = TextInput(hint_text="Height")
        height_unit_box = BoxLayout()
        self.height_cm = ToggleButton(text="cm", group="height", state='down')
        self.height_in = ToggleButton(text="inch", group="height")
        height_unit_box.add_widget(self.height_cm)
        height_unit_box.add_widget(self.height_in)

        self.weight_input = TextInput(hint_text="Weight")
        weight_unit_box = BoxLayout()
        self.weight_kg = ToggleButton(text="kg", group="weight", state='down')
        self.weight_lb = ToggleButton(text="lb", group="weight")
        weight_unit_box.add_widget(self.weight_kg)
        weight_unit_box.add_widget(self.weight_lb)

        submit_btn = Button(text="Next")
        submit_btn.bind(on_press=self.save)

        layout.add_widget(Label(text="Enter Your Info"))
        layout.add_widget(self.name_input)
        layout.add_widget(self.age_input)
        layout.add_widget(self.sex_label)
        layout.add_widget(sex_box)
        layout.add_widget(Label(text="Height"))
        layout.add_widget(self.height_input)
        layout.add_widget(height_unit_box)
        layout.add_widget(Label(text="Weight"))
        layout.add_widget(self.weight_input)
        layout.add_widget(weight_unit_box)
        layout.add_widget(submit_btn)

        self.add_widget(layout)

    def save(self, instance):
        try:
            user_data = users_data[current_user]  # ✅ Fetch data for logged-in user
            user_data['name'] = self.name_input.text
            user_data['age'] = int(self.age_input.text)
            user_data['sex'] = 'male' if self.male.state == 'down' else 'female'
            user_data['height_value'] = float(self.height_input.text)
            user_data['height_unit'] = 'cm' if self.height_cm.state == 'down' else 'inch'
            user_data['weight_value'] = float(self.weight_input.text)
            user_data['weight_unit'] = 'kg' if self.weight_kg.state == 'down' else 'lb'

            print("[DEBUG] User input collected:")
            for key, val in user_data.items():
                print(f"  {key}: {val}")

            save_all_users()  # ✅ Save the update
            self.manager.current = 'review'

        except Exception as e:
            print(f"[ERROR] Invalid input: {e}")


class ReviewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.info_label = Label(text="")
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(self.info_label)

        continue_btn = Button(text="Continue")
        continue_btn.bind(on_press=self.go_next)
        layout.add_widget(continue_btn)

        self.add_widget(layout)

    def on_enter(self):
        global current_user
        if current_user in users_data:
            u = users_data[current_user]
            self.info_label.text = (
                f"Name: {u.get('name', '[No Name]')}\n"
                f"Age: {u.get('age', '[Unknown]')}\n"
                f"Sex: {u.get('sex', '[Unknown]')}\n"
                f"Height: {u.get('height_value', 0)} {u.get('height_unit', 'cm')}\n"
                f"Weight: {u.get('weight_value', 0)} {u.get('weight_unit', 'kg')}"
            )
        else:
            self.info_label.text = "[ERROR] No user data found."

    def go_next(self, instance):
        self.manager.current = 'recommendation'



class RecommendationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.info_label = Label(text="")
        self.layout.add_widget(self.info_label)
        next_btn = Button(text="Next")
        next_btn.bind(on_press=self.go_next)
        self.layout.add_widget(next_btn)
        self.add_widget(self.layout)

    def on_enter(self):
        bmi, goal, calories, water, sleep = calculate_recommendations()
        self.info_label.text = (
            f"BMI: {bmi}\n"
            f"Goal: {goal}\n"
            f"Calories/day: {calories} kcal\n"
            f"Water/day: {water} L\n"
            f"Sleep: {sleep}"
        )

    def go_next(self, instance):
        self.manager.current = 'day_selection'

class DaySelectionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.day_buttons = {}
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        self.layout.add_widget(Label(text="Select Workout Days:"))
        for day in self.days:
            btn = ToggleButton(text=day)
            self.day_buttons[day] = btn
            self.layout.add_widget(btn)

        select_all = Button(text="Select All")
        select_all.bind(on_press=self.select_all_days)

        next_btn = Button(text="Next")
        next_btn.bind(on_press=self.generate_plan)

        self.layout.add_widget(select_all)
        self.layout.add_widget(next_btn)
        self.add_widget(self.layout)

    def select_all_days(self, instance):
        for btn in self.day_buttons.values():
            btn.state = 'down'

    def generate_plan(self, instance):
        selected = [day for day, btn in self.day_buttons.items() if btn.state == 'down']
        if selected:
            user_data = users_data[current_user]  # ✅ get the current user's data

            user_data['workout_days'] = selected
            user_data['plan_progress'] = {
                day: {"exercises": random.sample(list(exercise_presets.items()), 4), "checked": []}
                for day in selected
            }

            save_all_users()  # ✅ save all user data
            self.manager.current = 'weekly_plan'


class WeeklyPlanScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.day_label = Label(text="")
        self.layout.add_widget(self.day_label)
        self.exercise_box = BoxLayout(orientation='vertical', spacing=10)
        self.layout.add_widget(self.exercise_box)

        self.finish_btn = Button(text="Finish")
        self.finish_btn.bind(on_press=self.finish_day)
        self.layout.add_widget(self.finish_btn)

        self.add_widget(self.layout)
        self.current_day_index = 0

    def on_enter(self):
        self.current_day_index = 0
        self.load_day()

    def load_day(self):
        self.exercise_box.clear_widgets()
        user_data = users_data[current_user]  # ✅ get current user data

        if self.current_day_index >= len(user_data['workout_days']):
            self.day_label.text = "🎉 You finished all workouts!"
            self.finish_btn.disabled = True
            self.finish_btn.opacity = 0
            btn_box = BoxLayout(size_hint_y=None, height=50, spacing=10)
            next_week = Button(text="Next Week")
            exit_btn = Button(text="Exit")
            next_week.bind(on_press=self.goto_day_selection)
            exit_btn.bind(on_press=self.exit_app)
            btn_box.add_widget(next_week)
            btn_box.add_widget(exit_btn)
            self.exercise_box.add_widget(btn_box)
            return

        self.finish_btn.disabled = False
        self.finish_btn.opacity = 1

        day = user_data['workout_days'][self.current_day_index]
        self.day_label.text = f"Plan for {day}"
        self.checkboxes = []

        for name, reps in user_data['plan_progress'][day]['exercises']:
            row = BoxLayout(size_hint_y=None, height=40)
            cb = CheckBox()
            label = Label(text=f"{name}: {reps}")
            row.add_widget(cb)
            row.add_widget(label)
            self.checkboxes.append(cb)
            self.exercise_box.add_widget(row)

    def finish_day(self, instance):
        if all(cb.active for cb in self.checkboxes):
            self.current_day_index += 1
        save_all_users()  # ✅ Use the new save method
        self.load_day()

    def goto_day_selection(self, instance):
        self.manager.current = 'day_selection'

    def exit_app(self, instance):
        App.get_running_app().stop()


class BeAManApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))         # ← ADD THIS
        sm.add_widget(TitleScreen(name='title'))
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(ReviewScreen(name='review'))
        sm.add_widget(RecommendationScreen(name='recommendation'))
        sm.add_widget(DaySelectionScreen(name='day_selection'))
        sm.add_widget(WeeklyPlanScreen(name='weekly_plan'))
        return sm


if __name__ == '__main__':
    BeAManApp().run()
