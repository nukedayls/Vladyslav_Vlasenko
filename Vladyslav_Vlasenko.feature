Feature: Testing EPAM website

    Scenario: epam_is_loaded
        Given browser is opened
        When go to "https://www.epam.com/"
        Then "https://www.epam.com/" will open in browser
    
    Scenario: website_reloaded
        Given "https://www.epam.com/" is opened
        When press "F5" on keyboard
        Then site will reload

    Scenario: open_fullscreen
        Given "https://www.epam.com/" is opened
        When press "F11" on keyboard
        Then site will open fullscreen

    Scenario: change_scale
        Given "https://www.epam.com/" is opened
        When reduce browser scale
        Then site will reduce its scale

    Scenario: open_insights  
        Given "https://www.epam.com/" is opened
        When push button named "Careers"
        Then page readresses to "https://www.epam.com/insights"

    Scenario Outline: change_language
        Given "https://www.epam.com/" is opened
        When press "Global (EN)" button
        And select <language>
        Then page in <language> will be loaded
        Examples:
        |India (English|
        |Hungary (English)|
        |Polska (Polski)|
        |Україна (Українська)|
    
    Scenario Outline: readress_to_sphere_is_working_on
        Given "https://www.epam.com/" is opened
        When press button "{sphere}"
        Then site readress  to "https://www.epam.com/services/{sphere}"
        Examples:
        |   sphere     |
        |   engineer   |
        |   operate    |
        |   optimize   |

    Scenario Outline: entering_any_adress_in_domain
        Given "https://www.epam.com/" is opened
        When go to site "https://www.epam.com/{domain}"
        Then site will open error 404 in EPAM domain
        Examples:
        |   aaaaaaa    |
        |   dasd       |
        |   asdasd     |
        |   asdadw     |
