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
  - [Other Features](#other-features)
- [Data Model](#data-model)
- [Logic](#logic)
- [Technology & Resources](#technology--resources)
- [Deployment](#deployment)
- [Issues/Bugs](#issuesbugs)
  - [Resolved](#resolved)
  - [Unresolved](#unresolved)
- [Testing & Validation](#testing--validation)
  - [Functional Testing](#functional-testing)
  - [WAVE Testing](#wave-testing)
  - [PageSpeed Testing](#pagespeed-testing)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#html-validation)
  - [JS Validation](#html-validation)
  - [Python Validation](#html-validation) 
- [Future Improvements/Developments](#future-improvementsdevelopments)
- [Acknowledgments](#acknowledgments)

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
- To allow users to book a table for their desired time and date, using a user friendly form.
- To show the user the restaurant's menu, including the ability to filter by allergens.
- To give the user a way of contacting the restaurant directly with any questions/queries.
- To allow users to create an account, allowing them to see any current reservations they have.
- To also allow users to edit and delete their reservations simply.

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

[The Kanban board for this project can be seen here.](https://github.com/users/DiarmuidHenry/projects/2)

All __must have__ user stories were acheived, as well as all but one __should have__. The only __could have__ task was not completed, as the amount of time and resources needed in order to fulfill it would vastly outweigh the minor benefit it would bring.

### Wireframes

HOME PAGE 
MAKE A RESERVATION
MENU
CONTACT
MY RESERVATIONS

### Images

- Hero/Background Image

This image was used to show the stylish interior of the restaurant, in order to give the user an impression of the ambience and feel of the place. This paired with the translucent page gives an overall sleek look to the site.

- Example/s of food images

These are used simply to show the user what each dish looks like.

### Colour Scheme

Pastel colours, that match the styling and ambience of the restaurant, SOMETHING SOMETHING

## Data Models

I created 2 separate apps in this project: _Booking_ and _Allergens_.

_Booking_ handled all of the data and logic involved in reservations. _Allergens_ handled all of the data and logic involved in the menu.

### Booking

ERD - BOOKING

The _Booking_ app manages the reservation system, including table availability, opening hours, and user bookings. Below is a breakdown of the models, their attributes, CRUD implementation, and superuser privileges/abilities.

#### Booking - Models

**NormalOpeningHours**
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

**ExceptionalOpeningHours**
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

**RestaurantTable**
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

**Reservation**
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

### Allergens

ERD - ALLERGENS

The _Allergens_ app manages menu items and their associated allergen information, allowing users to filter menu options based on dietary restrictions. Below is a breakdown of the models, their attributes, CRUD implementation, and user-friendly data input capabilities through the admin panel.

#### Allergen - Model

**MenuItem**
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

## Logic

### Booking

Flowchart, for the process of making and cancelling a booking (and how data from different models is called).

### Allergens

Flowchart, for the process of using filters, as well as making new entries in the database.

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
4. In the **KEY** field, enter the secret/sensitive variable names that you have/will store in your `env.py` file. For example, `DATABASE_URL`. \
In the corresponding `VALUE` field, enter the value for these variables. For example, `postgres://<sensitive_information_included_here>/<your_database_name>`.
5. Go to the **Deploy** tab. Beside **Deployment method**, click **GitHub**, then confirm by clicking **Connect to GitHub**.
6. Under **Search for a repository to connect to**, type the name of the repo (whether that be the name of this repo, or of the one you have cloned). Click **Search**, then click **Connect** when the repo name appears. The Heroku app is now linked to the GitHub repo.
7. If you would like Heroku to manually update the app every time you push chances to GitHub, click on **Enable Automatic Deploys**. (This is optional).
8. Deploy the app by scrolling down and clicking **Deploy Branch**. Heroku will show you the deployment logs as it builds the app. This will take a few seconds.
9. When the app is finished being built, a message will appear saying **Your app was successfully deployed**. Click the **View** button to view the app (opens in a new tab).

## Issues/Bugs

### Resolved

- List of bugs
- Screenshots included (collapsable?)

### Unresolved

- Things that I want to develop in the future?
- This whatever doesnt work

## Testing & Validation

### Manual Functional Testing

Manual testing table for every functionality in the website (lots of work, but most will be repeats of simple commands). Table format, use earlier project as template.

### PageSpeed Testing

### WAVE Testing

### HTML

Run finished project through validator, include screenshot.

### CSS

Run finished project through validator, include screenshot.

### JS

Run finished project through validator, include screenshot.

### Python

Run finished project through validator, include screenshot.

## Future Improvements/Developments

- Add possibility for user to select several tables when booking for a larger group.
- Cascade for when the opening hours are changed, affecting an already existing reservation. SHOULD I DO THIS?

## Acknowledgments

- Student Care
- Mentor
