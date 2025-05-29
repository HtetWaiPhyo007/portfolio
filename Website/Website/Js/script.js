document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggle-theme');
    const toggleLanguageButton = document.getElementById('toggle-language');
    const body = document.body;
    const moonIcon = 'fas fa-moon'; // Class for moon icon
    const sunIcon = 'fas fa-sun';   // Class for sun icon

    const englishTexts = {
        // Common across pages
        homeMenu: "Home",
        historyMenu: "History",
        cultureMenu: "Culture",
        geographyMenu: "Geography",
        travelMenu: "Travel Info",
        

        // Index page
        welcomeTitle: "Welcome to Myanmar",
        aboutTitle: "About Myanmar",
        aboutDescription: "Myanmar, officially known as the Republic of the Union of Myanmar, is a country in Southeast Asia.",

        // History page
        historyTitle: "Myanmar History",
        historyOverviewTitle: "Historical Overview",
        historyDescription: "Myanmar's history is one of resilience in the face of colonialism, internal conflict, and military rule. It has a rich cultural heritage, rooted in Buddhism and the legacy of its ancient kingdoms, but the country continues to struggle with political instability and ethnic divisions. The road to lasting peace and democracy remains challenging.",

        // Culture page
        cultureTitle: "Myanmar Culture",
        cultureOverviewTitle: "Culture and Traditions",
        cultureDescription: "Explore Myanmar's rich culture, including its festivals, food, and traditional practices.",

        // Geography page
        geographyTitle: "Myanmar Geography",
        geographyOverviewTitle: "Geographical Features",
        geographyDescription: "Information about Myanmar's landscape, major cities, and natural landmarks.",

        // Travel page
        travelTitle: "Travel Information",
        travelOverviewTitle: "Travel Tips and Information",
        travelDescription: "Find out essential travel information for Myanmar, including visa requirements and top attractions."
    };

    const japaneseTexts = {
        // Common across pages
        homeMenu: "ホーム",
        historyMenu: "歴史",
        cultureMenu: "文化",
        geographyMenu: "地理",
        travelMenu: "旅行情報",
        

        // Index page
        welcomeTitle: "ミャンマーへようこそ",
        aboutTitle: "ミャンマーについて",
        aboutDescription: "ミャンマーは、正式にはミャンマー連邦共和国と呼ばれ、東南アジアに位置する国です。",

        // History page
        historyTitle: "ミャンマーの歴史",
        historyOverviewTitle: "歴史的概要",
        historyDescription: "ミャンマーの歴史は、植民地主義、内部紛争、軍政に直面しながらも、しぶとく生き延びてきた歴史です。仏教や古代王国の遺産に根ざした豊かな文化遺産を持つ一方で、政治的不安定や民族的な対立に苦しんでいます。持続的な平和と民主主義への道は依然として困難な状況にあります。",

        // Culture page
        cultureTitle: "ミャンマーの文化",
        cultureOverviewTitle: "文化と伝統",
        cultureDescription: "ミャンマーの豊かな文化、祭り、食べ物、伝統的な習慣を探検しましょう。",

        // Geography page
        geographyTitle: "ミャンマーの地理",
        geographyOverviewTitle: "地理的特徴",
        geographyDescription: "ミャンマーの地形、主要都市、自然の名所についての情報。",

        // Travel page
        travelTitle: "旅行情報",
        travelOverviewTitle: "旅行のヒントと情報",
        travelDescription: "ビザの要件や主要な観光スポットなど、ミャンマーの重要な旅行情報を見つけましょう。"
    };

    let currentLanguage = 'english';

    // Check local storage for the theme preference
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-mode');
        toggleButton.querySelector('i').className = sunIcon;
    } else {
        body.classList.remove('dark-mode');
        toggleButton.querySelector('i').className = moonIcon;
    }

    // Toggle theme on button click
    toggleButton.addEventListener('click', function() {
        if (body.classList.contains('dark-mode')) {
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
            toggleButton.querySelector('i').className = moonIcon;
        } else {
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
            toggleButton.querySelector('i').className = sunIcon;
        }
    });

    // Function to switch between English and Japanese
    const switchLanguage = () => {
        const texts = currentLanguage === 'english' ? japaneseTexts : englishTexts;

        // Update common elements
        document.getElementById('home-menu').textContent = texts.homeMenu;
        document.getElementById('history-menu').textContent = texts.historyMenu;
        document.getElementById('culture-menu').textContent = texts.cultureMenu;
        document.getElementById('geography-menu').textContent = texts.geographyMenu;
        document.getElementById('travel-menu').textContent = texts.travelMenu;
        document.getElementById('footer-text').innerHTML = texts.footerText;

        // Update page-specific elements
        if (document.getElementById('welcome-title')) {
            document.getElementById('welcome-title').textContent = texts.welcomeTitle;
            document.getElementById('about-title').textContent = texts.aboutTitle;
            document.getElementById('about-description').textContent = texts.aboutDescription;
        } else if (document.getElementById('history-title')) {
            document.getElementById('history-title').textContent = texts.historyTitle;
            document.getElementById('history-overview-title').textContent = texts.historyOverviewTitle;
            document.getElementById('history-description').textContent = texts.historyDescription;
        } else if (document.getElementById('culture-title')) {
            document.getElementById('culture-title').textContent = texts.cultureTitle;
            document.getElementById('culture-overview-title').textContent = texts.cultureOverviewTitle;
            document.getElementById('culture-description').textContent = texts.cultureDescription;
        } else if (document.getElementById('geography-title')) {
            document.getElementById('geography-title').textContent = texts.geographyTitle;
            document.getElementById('geography-overview-title').textContent = texts.geographyOverviewTitle;
            document.getElementById('geography-description').textContent = texts.geographyDescription;
        } else if (document.getElementById('travel-title')) {
            document.getElementById('travel-title').textContent = texts.travelTitle;
            document.getElementById('travel-overview-title').textContent = texts.travelOverviewTitle;
            document.getElementById('travel-description').textContent = texts.travelDescription;
        }

        currentLanguage = currentLanguage === 'english' ? 'japanese' : 'english';
    };

    // Toggle language on button click
    toggleLanguageButton.addEventListener('click', switchLanguage);
});

document.addEventListener('DOMContentLoaded', () => {
    // Select all images on the page
    const images = document.querySelectorAll('img');

    // Apply styles to each image
    images.forEach(image => {
        image.style.maxWidth = '100%';  // Responsive sizing
        image.style.height = 'auto';    // Maintain aspect ratio
        image.style.borderRadius = '10px';  // Rounded corners
        image.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';  // Add a subtle shadow
        image.style.margin = '20px 0';  // Add margin around the image
        image.style.transition = 'transform 0.3s ease';  // Smooth transition for hover effect

        // Add a hover effect to scale up the image slightly
        image.addEventListener('mouseover', () => {
            image.style.transform = 'scale(1.05)';  // Slight zoom on hover
        });

        image.addEventListener('mouseout', () => {
            image.style.transform = 'scale(1)';  // Reset to original size when not hovering
        });
    });
});
document.addEventListener('DOMContentLoaded', () => {
    // Select all images on the page
    const images = document.querySelectorAll('img');

    // Function to reveal an image when it enters the viewport
    const revealImage = (image) => {
        const rect = image.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom >= 0) {
            image.style.opacity = '1';  // Fade in the image
            image.style.transform = 'translateY(0)';  // Slide to original position
        }
    };

    // Apply initial styles and set up scroll event listener
    images.forEach(image => {
        // Initial styling for responsive and aesthetic appearance
        image.style.maxWidth = '100%';  // Responsive sizing
        image.style.height = 'auto';    // Maintain aspect ratio
        image.style.borderRadius = '10px';  // Rounded corners
        image.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';  // Add a subtle shadow
        image.style.margin = '20px 0';  // Add margin around the image
        
        // Initial transform and transition for animation effect
        image.style.opacity = '0';  // Initially hidden
        image.style.transform = 'translateY(20px)';  // Start from lower position
        image.style.transition = 'opacity 1s ease-out, transform 1s ease-out';  // Animation duration and easing

        // Check the image position on page load
        revealImage(image);

        // Set up a scroll event listener to reveal images
        window.addEventListener('scroll', () => revealImage(image));
    });
});






