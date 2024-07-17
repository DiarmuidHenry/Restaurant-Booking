# BigByte Restaurant

This project is a Django based website that handles bookings for a restaurant. Users sign up and can see and delete their reservations, with the database being updated accordingly. The website also allows users to see the menu, filtering the results by allergens and dietary preferences.

IMAGE OF WEBSITE ON DIFFERENT DEVICES

[Deployed Website](https://restaurant--booking-465b6b7fd829.herokuapp.com/)

## Table of Contents

- [Goals](#goals)
- [Key Features](#key-features)
- [Potential Users](#potential-users)
- [UX Design & Development](#ux-design--development)
  - [Agile Development](#agile-development)
  - [Wireframes](#wireframes)
  - [Images](#images)
  - [Colour Scheme](#colour-scheme)
- [Data Model](#data-model)
  - [Booking](#booking)
  - [Allergens](#allergens)
- [Logic](#logic)
  - [Booking](#booking-logic)
  - [Allergens](#allergens-logic)
- [Technology & Resources](#technology--resources)
- [Deployment](#deployment)
  - [How to Clone Repository](#how-to-clone-repository)
  - [How to Deploy to Heroku](#how-to-deploy-to-heroku)
- [Issues/Bugs](#issuesbugs)
  - [Resolved](#resolved)
  - [Unresolved](#unresolved)
- [Testing & Validation](#testing--validation)
  - [Manual Functional Testing](#manual-functional-testing)
  - [PageSpeed Testing](#pagespeed-testing)
  - [WAVE Testing](#wave-testing)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JS Validation](#js-validation)
  - [Python Validation](#python-validation)
- [Future Improvements/Developments](#future-improvementsdevelopments)
- [Acknowledgments](#acknowledgments)


## Goals

- To build a functioning website for a restaurant.
- To allow users to book a table for their desired time and date, using a user friendly form.\
[EPIC: Reservations](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/20)\
This should also take opening hours into consideration: both standard opening hours, but also special opening hours such as holidays.\
It should also allow users to edit and delete their reservations simply.
[EPIC: Opening Hours](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/11)
- To show the user the restaurant's menu, including the ability to filter by allergens.\
[EPIC: Online Menu](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/28)
- To give the user a way of contacting the restaurant directly with any questions/queries.\
[EPIC: Contact Form](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/35)
- To allow users to create an account, allowing them to see any current reservations they have.


## Key Features

- INCLUDE SCREENSHOTS

- Large, clear images of the restaurant to show the user the interior.
- _Make a Reservation_ page, where users can make a reservation by filling out the booking form.
- _My Reservations_ page, where users can see their reserevations, past and present.
- Thanks/Confirmation pages, to confirm to the user that their action has been completed.
- Confirmation emails, as permanent evidence of such changes.
- _Contact_ page, for users to directly contact the restaurant by filling out a simple message form.
- _Menu_, where users can see the entire menu, as well as having the ability to filter the menu by the allergens that apply to them/their co-diners. Users can also click on each item to see an enlarged image.
- _Make A Reservation_ buttons appearing regularly, giving the user an easy path to booking a table.

## Potential Users

- Regulars of the restaurant.
- Potential future diners, curious about the ambience/style.
- Users with allergies, who want to research their meal beforehand.

## UX Design & Development

### 5 Layers of UX

I began the development by considering the 5 layers of UX and how those would shape the content and appearance of the website.

#### Strategy

The UX strategy for the restaurant website focuses on optimising the booking experience whilst also giving the user a specialised/tailored view of the restaurant's menu.  The ever growing need for clear allergen information led me to make this a key feature in the menu section of the project, as this is often overlooked, even considering that this is an increasing proportion of the general public.

#### Scope

I prioritised extra functionalities such as seat selection during booking, as well as reservation editing and cancellation options to enhance user control and convenience, which are not prevelant on most other restaurant booking/reservation systems. This was to give the user more control over their reservation, thereby improving the customisability of the user's experience.

Highlighting allergy information and giving users the ability to enter their relevant allergens and filter such dishes from the menu, allows allergen afflicted users to feel more confident/comfortable before and during their dining experience (which can often be uncomfortable where limited information is available).

#### Structure

The user is clearly guided through the different areas of the website by the navbar, which is viewable and accessible on all devices. The structure of the website is designed to provide an intuitive and seamless user experience, ensuring that users can effortlessly navigate through the various sections. Each link in the navbar is labeled to provide immediate understanding of its destination, reducing the cognitive load on users and helping them find the information they need quickly.

The user starts on a clean, sleek home page where the navbar clearly shows the different functions of the site. When the user clicks on Sign In or Sign Up, they are informed that it is necessary to do so in order to make a reservation. The Make a Reservation page presents an easy-to-understand form for entering booking details and requests, leading to the desired booking or directing users to the Contact page to message the restaurant directly. The My Reservations page lists the main details of the user's reservations and provides options to edit or cancel them. The Menu page highlights the option to filter by allergen or dietary requirement, with large, clear images that can be clicked to enlarge, allowing diners to get a feel for the dishes.

#### Skeleton

The skeleton of the website is based around wireframes that define the layout and key interactions of the site. The homepage features a clean design with prominent links for signing in, signing up, and making reservations. Simple and straightforward forms for sign-in and sign-up guide users through account creation and access, which are essential for making reservations.

The Make a Reservation page includes an intuitive form for entering booking details, complete with validation to ensure all necessary information is provided and a redirect to the Contact page if needed. The My Reservations page organizes users' bookings in a neat table, with options to edit or cancel, facilitating easy management of reservations. The Menu page is structured with clear sections and high-quality images, featuring filters for allergens and dietary requirements.

[See Wireframes below](#wireframes).

#### Surface

The surface design of the restaurant website focuses on visual appeal and a calm, professional, sleek look to enhance user engagement. The homepage features a clean, modern design, including a muted colour palette and a high quality image of the interior of the restaurant that reflects the dining experience.

Interactive elements such as buttons and links have been styled to be easily identifiable and clickable.

The _Make a Reservation_ and _My Reservations_ pages use a clean, uncluttered design to present forms and information clearly, making the booking process straightforward and user-friendly.

The _Menu_ page showcases dishes with large, clear images that can be clicked to enlarge, accompanied by well-structured text detailing ingredients and dietary information. 

Overall, the visual design is crafted to be responsive, ensuring that the website looks and functions well on all devices, from desktops to smartphones, while maintaining a consistent and inviting aesthetic throughout.

### Agile Development

The project was planned, tracked and process using the AGILE methodology throughout.

I initially created a small number of epics, each of which consisted of multiple user stories. In turn, these user stories were defined and check based on multiple acceptance criteria, ensuring that the desired result from that user story was acheived.

[The Kanban board for this project can be seen here.](https://github.com/users/DiarmuidHenry/projects/2) Below are direct links to all epics and the user stories they consist of:

[EPIC: Admin/Housekeeping](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/34)

 - [USER STORY: Project Creation](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/30)
 - [USER STORY: README.md](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/31)
 - [USER STORY: Heroku Deployment](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/32)
 - [USER STORY: Testing](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/33)

[EPIC: Opening Hours](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/11)

 - [USER STORY: Establish Normal Opening Hours](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/13)
 - [USER STORY: Establish Exceptional Opening Hours](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/14)

[EPIC: Reservations](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/20)

 - [USER STORY: Booking Form](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/17)
 - [USER STORY: Choice of Table](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/18)
 - [USER STORY: Confirmation Email](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/19)
 - [USER STORY: Editing a Reservation](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/16)
 - [USER STORY: Cancelling a Reservation](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/15)
 - [USER STORY: Navigating to 'Make a Reservation'](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/21)
 - [USER STORY: User Account](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/22)
 - [USER STORY: Updating Restaurant Information](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/25)
 - [USER STORY: Updating Databases on Website](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/26)
 - [USER STORY: Filling out the Booking Form](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/27)

[EPIC: Online Menu](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/28)

 - [USER STORY: Viewing the Menu](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/23)
 - [USER STORY: Allergens](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/24)
 - [USER STORY: Updating Restaurant Information](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/25)
 - [USER STORY: Updating Databases on Website](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/26)

[EPIC: Contact Form](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/35)

 - [USER STORY: Creating Contact Form](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/38)
 - [USER STORY: Pre-populating User Information](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/36)
 - [USER STORY: Pre-populating Relevant Subject/Message](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/37)


All __must have__ user stories were acheived, as well as almost all __should have__ user stories. The only __could have__ task was not completed, as the amount of time and resources needed in order to fulfill it would vastly outweigh the minor benefit it would bring.

### Wireframes

HOME PAGE 
MAKE/EDIT A RESERVATION
MENU
CONTACT
MY RESERVATIONS

### Images

![Background Image](/media/readme-images/background_image.jpg)


This image was used to show the stylish interior of the restaurant, in order to give the user an impression of the ambience and feel of the place. This paired with the translucent page gives an overall sleek look to the site.

EXAMPLE OF FOOD IMAGE

These are used simply to show the user what each dish looks like. It also adds colour and vibrance to the page.

### Colour Scheme

![Colour Palette](/media/readme-images/restaurant_colours.png)

I chose a simple, muted beige colour scheme. I wanted to create a calming effect, so fewer more subtle colours was the way to acheive this. The auburn/brown colour is used only for buttons, to highlight their position.

## Data Models

I created 2 separate apps in this project: _Allergens_ and _Booking_.

### Allergens

![ERD Allergens](/media/readme-images/erd_allergens.png)

The _Allergens_ app manages menu items and their associated allergen information, allowing users to filter menu options based on dietary restrictions. Below is a breakdown of the models, their attributes, CRUD implementation, and user-friendly data input capabilities through the admin panel.


#### MenuItem

  - **Attributes**:
      - `dish_name`: TextField
      - `description`: TextField
      - `section`: CharField (choices: Starters, Mains, Sides, Kids, Desserts, default: Mains)
      - `price`: DecimalField (max_digits: 10, decimal_places: 2, default: 0.00)
      - `gluten`: BooleanField (default: False)
      - `crustaceans`: BooleanField (default: False)
      - `eggs`: BooleanField (default: False)
      - `fish`: BooleanField (default: False)
      - `peanuts`: BooleanField (default: False)
      - `soy`: BooleanField (default: False)
      - `dairy`: BooleanField (default: False)
      - `nuts`: BooleanField (default: False)
      - `celery`: BooleanField (default: False)
      - `mustard`: BooleanField (default: False)
      - `sesame`: BooleanField (default: False)
      - `sulphites`: BooleanField (default: False)
      - `lupin`: BooleanField (default: False)
      - `molluscs`: BooleanField (default: False)
      - `vegan`: BooleanField (default: False)
      - `vegetarian`: BooleanField (default: False)
      - `image`: CloudinaryField (null=True)
      - `slug`: SlugField (unique=True, blank=True)

  - **CRUD Implementation**:
      - **Create**: Superusers can add new menu items, specifying dish details and allergens.
      - **Read**: Users can view menu items and filter by allergen tags.
      - **Update**: Superusers can update menu item details, including allergen information.
      - **Delete**: Superusers can delete menu items no longer offered.

  - **Usage**: MenuItem stores details about each dish, including its name, description, price, allergens, and dietary preferences.

### Booking

![ERD Booking](/media/readme-images/erd_booking.png)

The _Booking_ app manages the reservation system, including table availability, opening hours, and user bookings. Below is a breakdown of the models, their attributes, CRUD implementation, and superuser privileges/abilities.

#### NormalOpeningHours

  - **Attributes**:
      - `day`: CharField (choices: Monday-Sunday)
      - `is_open`: BooleanField (default: False)
      - `opening_time`: TimeField
      - `closing_time`: TimeField

  - **CRUD Implementation**:
      - **Create**: Superusers can set regular opening hours for each day of the week.
      - **Read**: Users can view normal opening hours to know standard booking times.
      - **Update**: Superusers can update regular opening hours as needed.
      - **Delete**: Superusers can remove or change specific opening time entries.

  - **Usage**: NormalOpeningHours defines daily opening hours for the restaurant. If ExceptionalOpeningHours for a specific date isn't defined, the system defaults to NormalOpeningHours.

#### ExceptionalOpeningHours

  - **Attributes**:
      - `date`: DateField (unique)
      - `is_open`: BooleanField (default: False)
      - `opening_time`: TimeField (nullable)
      - `closing_time`: TimeField (nullable)

  - **CRUD Implementation**:
      - **Create**: Superusers can set exceptional opening hours for specific dates.
      - **Read**: Through the booking portal, users can view exceptional opening hours for special dates.
      - **Update**: Superusers can update exceptional opening hours as needed.
      - **Delete**: Superusers can remove or change specific hours.

  - **Usage**: ExceptionalOpeningHours allows defining special opening hours for specific dates, overriding NormalOpeningHours if present.

#### RestaurantTables

  - **Attributes**:
      - `table_number`: PositiveIntegerField (unique)
      - `capacity`: PositiveIntegerField (validators: MinValueValidator(1))
      - `table_location`: CharField (choices: Inside, Outside, default: Inside)

  - **CRUD Implementation**:
      - **Create**: Superusers can add new tables with specific seat numbers.
      - **Read**: Users can see available tables and their capacity when making a reservation.
      - **Update**: Superusers can update table details (e.g., number of seats, location).
      - **Delete**: Superusers can remove tables no longer in use.

  - **Usage**: RestaurantTable defines the available tables, their location and their capacities for seating guests.

#### Reservation

  - **Attributes**:
      - `reservation_id`: AutoField (primary_key)
      - `user`: ForeignKey (to User model, nullable)
      - `first_name`: CharField (max_length: 25, default: '')
      - `last_name`: CharField (max_length: 25, default: '')
      - `email`: EmailField (default: '')
      - `table`: ForeignKey (to RestaurantTable)
      - `created_on`: DateTimeField (auto_now_add)
      - `reservation_date`: DateField
      - `reservation_length`: FloatField (choices: 1.0-3.0, default: 2.0)
      - `reservation_time`: TimeField
      - `number_of_guests`: PositiveIntegerField (validators: MinValueValidator(1), MaxValueValidator(50))
      - `table_location`: CharField (choices: Inside, Outside, default: Inside)
      - `reservation_end_time`: TimeField (nullable)
      - `message`: TextField (max_length: 200, blank=True, null=True)

  - **CRUD Implementation**:
      - **Create**: Users can create reservations by filling in a form.
      - **Read**: Users and superusers can view reservation details.
      - **Update**: Users can update their own reservations; superusers can update any reservation.
      - **Delete**: Users can cancel their own reservations; superusers can delete any reservation.

  - **Usage**: Reservation stores details about each booking, including guest information, table selection, and timing.


**Relationships**

- **NormalOpeningHours** and **ExceptionalOpeningHours**: Exceptional opening hours take precedence over Normal opening hours if defined for a specific date.
- **RestaurantTable** and **Reservation**: Ensures that tables are booked appropriately and no double bookings occur.
</details>

I also integrated the standard **Django Auth** module to create the User aspect, allowing users to sign in and out. This allowed me to link each reservation with the user that created it. More importantly, it alloewd me to add an authentication check when editing a reservation, to ensure that the only one who could edit a reservation (other than a superuser) is the person that created it.

## Logic

### Booking

This is the primary app used on the site, and contains all the functionality involved with the restaurant's reservations.

The main use of logic in the _Booking_ app is in the `check_availability` view. This takes the information that the user has entered into the _Make a Reservation_/_Edit Reservation_ form and returns all tables (if any) that match the user's input. It also prioritises smaller tables, to avoid (for example) a group of 2 booking a table for 8. In this case that no table is available, an alert message appears, directing the user to the _Contact_ page, where the information from the user's booking form (as well as their information stored in the User database) is prepopulated.

Below is a flowchart showing how the `check_availability` view functions.

![check_availibility Flowchart](/media/readme-images/check_availability_flowchart.png)

All other views and functions in this app are fairly straightforward, and are mainly concerned about managing the input from the user correctly. Since editing and making a reservation are similar processes, I combined these two functions into one view - `process_reservation` - with extra paramaters to distinguish each case.

### Allergens

The only logic used in this app is simply filtering menu items based on the boolean attributes stored in their corresponding entry in the _Menu Items_ database. When the user clicks on one or more allergens, the _Filter_ buttons removes any items containing these allergens from the HTML code that populates the _Menu_ page. The same logic applies to the dietary requirements, but in an opposite way: for example, clicking on _Vegetarian_ will only show dishes that **ARE** vegetarian.

## Technology & Resources

- **Django**: Web framework for backend development, providing a structured approach to building the restaurant website.
- **PostgreSQL**: Database management system for storing and managing restaurant data securely.
- **Cloudinary**: Cloud-based image and video management service used for handling images of menu items.
- **HTML/CSS/JavaScript**: Frontend technologies for creating interactive and responsive user interfaces.
- **Bootstrap**: Frontend framework for designing mobile-first and responsive websites.
- **Git/GitHub**: Version control system and platform for project management.
- **Heroku**: Cloud platform for deploying the application.
- **GitPod**: Online IDE for coding and devloping project.
- **Python Libraries**: Various Python libraries used for additional functionalities.
- **PEP8**: Python style guide used to ensure code readability and consistency.
- **WAVE Accessibility Tool**: Web accessibility evaluation tool for ensuring accessibility inclusive design practices.
- **W3C Validator**: Tools for validating HTML, CSS, and web standards used in website development.
- **dbdiagram.io**: ERD design.
- **Draw.io**: Flow chart design.
- **Pexels**: Royalty free images.
- **Microsoft Designer**: Creating the menu dish images (due to lack of real photos available).

## Deployment

### Heroku

### How to Clone Repository

1. Go to the [GitHub repository](https://github.com/DiarmuidHenry/Restaurant-Booking/).
2. Click the green **Code** drop down button.
3. Click **HTTPS** and copy the URL.
4. Open your IDE, and open a terminal.
5. Enter `git clone url`, replacing `url` with the URL copied in step 3.

### How to deploy to Heroku

1. Log in to [Heroku](https://www.heroku.com/). If you do not already have an account, you can [sign up here](https://signup.heroku.com/).
2. Click **Create new app** on the Heroku Dashboard. Give the app a unique name. Select your region, click **Create app**.
3. Go to the **Settings** tab, click on **Reveal Config Vars**
4. In the **KEY** field, enter the secret/sensitive variable names that you have/will store in your `env.py` file. For example, `DATABASE_URL`, `DEFAULT_FROM_EMAIL`. \
In the corresponding `VALUE` field, enter the value for these variables. For example, `postgres://<sensitive_information_included_here>/<your_database_name>`, `thisis@myemail.com`.
5. Go to the **Deploy** tab. Beside **Deployment method**, click **GitHub**, then confirm by clicking **Connect to GitHub**.
6. Under **Search for a repository to connect to**, type the name of the repo (whether that be the name of this repo, or of the one you have cloned). Click **Search**, then click **Connect** when the repo name appears. The Heroku app is now linked to the GitHub repo.
7. If you would like Heroku to manually update the app every time you push chances to GitHub, click on **Enable Automatic Deploys**. (This is optional).
8. Deploy the app by scrolling down and clicking **Deploy Branch**. Heroku will show you the deployment logs as it builds the app. This will take a few seconds.
9. When the app is finished being built, a message will appear saying **Your app was successfully deployed**. Click the **View** button to view the app (opens in a new tab).

## Issues/Bugs

### Resolved

- **Chosen allergens being reset on page reload**

  ![Chosen allergens reset](/media/readme-images/bug_filter_choices_lost_1.png)

  When a user navigated to the enlarged image and information of a menu item and then clicked _Back to Menu_, the chosen allergens/dietary requirements were erased, meaning they needed to be selected again.

  The solution to this was to store the chosen allergens in the url of both the main menu page, but also the detailed image/information page, meaning that the allergen/dietary requirement information could eaily be passed back and forth, meaning the user would not hav to re-input their choices.

  ![Chosen allergens stored](/media/readme-images/bug_filter_choices_lost_2.png)



### Unresolved

- Things that I want to develop in the future?
- This whatever doesnt work

## Testing & Validation

### Manual Functional Testing

Below are the records for the extensive manual testing of all functionalities of both the website and the database.

### Automated Testing

For this, I used the inbuilt testing module `unittest`. I tested the `menu_item_list` view in the _Allergens_ app. This is the view that controls the filtering of dishes containing certain allergens and whether they are vegan/vegetarian.

In order for an this test to pass, it needed the following:

- Fail if any of the inputs are not Boolean. The input into this function is a series of Boolean values stating whether certain allergens/dietary requirements apply or do not apply. If, for example, the function receives a float as one of the inputs, it should raise a `TypeError`.
- Fail if any of the inputs are of the type `None`, i.e. there is missing data. In order for the function to be accurate, an input must be received for each of the dietary criteria.
- If the input for an allergen **a** is `True`, then the return **must not** include any entries from the _MenuItem_ database that have the attribute `a` value set to `True`.
- If the input for an allergen **b** is `False`, then the return must not exclude any entries from the _MenuItem_ database based on their `b` value. For example, if you do **not** a _Peanut_ allergy, then the item's **Peanut** variable value is irrelevant; it must not affect the return. 
- If the input for **Vegetarian** is `True`, then the return **must not** include any entries from the _MenuItem_ database that have the attribute `vegetarian` value `False`.
- If the input for an **Vegetarian**** is `False`, then the return must not exclude any entries from the _MenuItem_ database based on their `vegetarian` value. If you are not a vegetarian, then the item's **Vegetarian** variable value is irrelevant; it must not affect the return. 
- If the input for **Vegan** is `True`, then the return **must not** include any entries from the _MenuItem_ database that have the attribute `vegan` value `False`.
- If the input for an **Vegan** is `False`, then the return must not exclude any entries from the _MenuItem_ database based on their `vegan` value. If you are not a vegan, then the item's **Vegan** variable value is irrelevant; it must not affect the return.

Whilst testing, one of my tests (`test_dietary_requirement_not_ticked_filtering`) failed repeatedly.

IMAGE HERE

After examining it further, the reason that it failed is due to the way the information is being passed. Since `default=True` for all of the allergen/dietary variables, they are simply not included in the url, if they are not selected. Hence, my search for `'?vegan=false'` could not exist in the actual application of the view `menu_list_item`. The way I solved this issue was to change the approach taken by the test. After ensuring the SetUp included both `vegan=True` and `vegan=False` values, I simply checked that no applying the `vegan` filter resulted in both vegan and non-vegan dishes being included in the response. The test passed.

### PageSpeed Testing

I have attached 2 images from PageSpeed testing that represent the scores that the website received. As there are a lot of different parts to the website, I have only included 2.

![PageSpeed Result - Home](/media/readme-images/pagespeed_home.png)

![PageSpeed Result - Allergens](/media/readme-images/pagespeed_allergens.png)

### WAVE Testing

Web Accessibility Evaluation Tools revealed 0 errors.

![WAVE Result](/media/readme-images/wave_result.png)

![WAVE Alerts](/media/readme-images/wave_alerts.png)

The 2 alerts are for the following:

- Skipped heading level: on some pages, there may be `<h1>` tags and `<h3>` tags, but no `<h2>` tags. Since this is part of the styling I have chosen, this is also by choice.
- _Home_ appears in the navbar, even when on the _Home_ page. This is by choice, for consistency in the styling and appearance of the navbar.

### HTML

All locations on the site passed HTML validation with no errors. Due to the way  Below are a few examples

### CSS

__style.css__

![CSS Validation](/media/readme-images/css_validation.png)

### JS

__get_opening_hours.js__

![JSHint Validation](/media/readme-images/js_authentication.png)

### Python

#### Allergens

__allergens/admin.py__

![Python Validation allergens/admin.py](/media/readme-images/lint_allergens_admin.png)

__allergens/models.py__

![Python Validation allergens/models.py](/media/readme-images/lint_allergens_models.png)

__allergens/urls.py__

![Python Validation allergens/urls.py](/media/readme-images/lint_allergens_urls.png)

__allergens/views.py__

![Python Validation allergens/views.py](/media/readme-images/lint_allergens_views.png)

#### Booking

__booking/admin.py__

![Python Validation booking/admin.py](/media/readme-images/lint_booking_admin.png)

__booking/context_processors.py__

![Python Validation booking/context_processors.py](/media/readme-images/lint_booking_context_processors.png)

__booking/forms.py__

![Python Validation booking/forms.py](/media/readme-images/lint_booking_forms.png)

__booking/models.py__

![Python Validation booking/models.py](/media/readme-images/lint_booking_models.png)

__booking/test.py__

![Python Validation booking/test.py](/media/readme-images/lint_booking_test.png)

__booking/urls.py__

![Python Validation booking/urls.py](/media/readme-images/lint_booking_urls.png)

__booking/views.py__

![Python Validation booking/views.py](/media/readme-images/lint_booking_views.png)


## Future Improvements/Developments

- Add possibility for user to select several tables when booking for a larger group. Although the current logic deals with this instance (and is arguably better and more flexible from the restaurant's point of view), I feel this would be a nice touch, and would give larger parties even more control over their dining experience.
- Cascade for when the opening hours are changed, affecting an already existing reservation. If, for example, the restaurant decides to begin closing early on Mondays or they decide to add an extra day to `ExceptionalClosingHours`, ideally a message should be sent to all future guests that have a reservation affected by this alteration (as well as to the restaurant to notify them of this). The current workaround would be to filter the existing reservations on the Django Admin panel and manually contact them (which is standard practise in most places), but an automated response would be more professional.
- Add logic to the _MenuItem_ database, so that any item with _Dairy_ or _Eggs_ set to `True`, automatically has _Vegan_ set to `False`. This should not be an issue if data is input correctly, but it gives the user less chance to introduce an error/inconsistency into the model.
- Assuming this was a real restaurant, I would hire a professional photographer to take real photos of the food, as opposes to [using generated images](#technology--resources).


## Acknowledgments

- **Student Care**: Quick responses and troubleshooting, especially when there were issues with the CI Database.
- **Mentor**: Having the ability to find broken logic and quickly point out areas that need improving.

