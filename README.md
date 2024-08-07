# BigByte Restaurant

This project is a Django based website that handles bookings for a restaurant: BigByte. Users sign up and can see, edit and delete their reservations, with the database being updated accordingly. The website also allows users to see the menu, filtering the results by allergens and dietary preferences.

![Homepage on Different Devices](/media/readme-images/homepage_different_devices.png)

[Deployed Website](https://restaurant--booking-465b6b7fd829.herokuapp.com/)

## Table of Contents

- [Goals](#goals)
- [Key Features](#key-features)
- [Potential Users](#potential-users)
- [UX Design & Development](#ux-design--development)
  - [5 Layers of UX](#5-layers-of-ux)
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
[EPIC: Opening Hours](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/11)\
It should also allow users to edit and delete their reservations simply.
- To show the user the restaurant's menu, including the ability to filter by allergens.\
[EPIC: Online Menu](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/28)
- To give the user a way of contacting the restaurant directly with any questions/queries.\
[EPIC: Contact Form](https://github.com/DiarmuidHenry/Restaurant-Booking/issues/35)
- To allow users to create an account, allowing them to see any current reservations they have.


## Key Features

- A clean, light _Home_ page with an image of the restaurant in the background. The background image remains in place when scrolling. The main content of each page appears in a container with soft, rounded corners. The navbar is fixed to the top, indicating to the user whether they are logged in or not. Note: _My Reservations_ only appears to those who are logged in.

![Home Page](/media/readme-images/homepage_top.png)

- Stylish images, again with rounded corners, accompany text telling the user about the restaurant's ethos.

![Home Page Images](/media/readme-images/homepage_images_text.png)

- Footer containing basic contact details, links to social media sites, and a list of opening hours. These opening hours are updated from the `NormalOpeningHours` database using a context processor, every time the page refreshes/loads.

![Footer](/media/readme-images/footer.png)

- _Make a Reservation_ page, where users can make a reservation by filling out the booking form.

![Make a Reservation page](/media/readme-images/make_a_reservation.png)

- _My Reservations_ page, where users can see their reservations, past and present. The link to this page is only seen by those who are logged in.

![My Reservations page](/media/readme-images/my_reservations_after.png)

- Thanks/Confirmation pages, to confirm to the user that their action has been completed.

![Reservation Confirmation page](/media/readme-images/reservation_creation_confirmation.png)

- Confirmation emails (both to the restaurant and the user), as evidence/a reminder of the user's reservation.

![Confirmation Email](/media/readme-images/reservation_creation_guest.png)

- _Contact_ page, for users (both those who are signed in and those who are not) to directly contact the restaurant by filling out a simple message form. If the user is signed in, the _First Name_, _Last Name_ and _Email_ fields are automatically populated with information from their user account.

![Contact Form](/media/readme-images/contact_form_signed_in.png)

- _Menu_, where users can see the entire menu, as well as having the ability to filter the menu by the allergens that apply to them/their co-diners.

![Menu Page](/media/readme-images/menu_items.png)

- Users can also click on each item to see an enlarged image. _Make A Reservation_ buttons appear regularly, giving the user an easy path to booking a table.

![Menu Item Details](/media/readme-images/menu_item_detailed.png)

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

I initially created a small number of epics, each of which consisted of multiple user stories. In turn, these user stories were defined and checked based on multiple acceptance criteria, ensuring that the desired result from that user story was acheived.

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

**Home Page**

![Wireframe - Home](/media/readme-images/wireframe_home.png)

**Make a Reservation**

![Wireframe - Make a Reservation](/media/readme-images/wireframe_booking_form.png)

**My Reservations**

![Wireframe - My Reservations](/media/readme-images/wireframe_my_reservations.png)

**Menu**

![Wireframe - Home](/media/readme-images/wireframe_menu.png)

### Images

![Background Image](/media/readme-images/background_image.jpg)

This image was used to show the stylish, relaxed interior of the restaurant, in order to give the user an impression of the ambience and feel of the place. This paired with the translucent page gives an overall sleek look to the site.

![Menu Item Details](/media/readme-images/menu_item_detailed.png)

These are used simply to show the user what each dish looks like. It also adds colour and vibrance to the page, and allows for easy booking with the _Make a Reservation_ button.

### Colour Scheme

![Colour Palette](/media/readme-images/restaurant_colours.png)

I chose a simple, muted beige/burgundy colour scheme. I wanted to create a calming effect, so fewer more subtle colours was the way to acheive this. The auburn/brown colour is used only for buttons, to highlight their position.

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
      - **Create**: Superusers can add new tables with correspoding capacities.
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

The main use of logic in the _Booking_ app is in the `check_availability` view. This takes the information that the user has entered into the _Make a Reservation_/_Edit Reservation_ form and returns all tables (if any) that match the user's input.

In order to remove the issue of 1 minute overlaps (a reservation from 14:00 - 15:30 and another from 15:30 - 17:30 should not count as overlapping), each reservation has 1 minute removed from the end when stored in the database. In this case, the first reservation's end time would have a value of 15:29.

It also prioritises smaller tables, to avoid (for example) a group of 2 booking a table for 8. In this case that no table is available, an alert message appears, directing the user to the _Contact_ page, where the information from the user's booking form (as well as their information stored in the User database) is prepopulated.

Below is a flowchart showing how the `check_availability` view functions.

![check_availibility Flowchart](/media/readme-images/check_availability_flowchart.png)

All other views and functions in this app are fairly straightforward, and are mainly concerned about managing the input from the user correctly. Since editing and making a reservation are similar processes, I combined these two functions into one view - `process_reservation` - with extra paramaters to distinguish each case.

Here is the flow/path through making, editing and cancelling a reservation:

- The user lands on the home page. In order to make a reservation, they click directly on the _Make a Reservation_ link in the navbar (or on any of the _Make a Reservation_ buttons that appear regularly throughout the site). After signing in (or signing up, and then signing in), they will be directed to the booking form.

- The user's basic contact information is automatically populated in the first fields.

- Since the restaurant is open at different hours on different days, the _Reservation Time_ slot is filled in dynamically. Once the user selects a _Reservation Date_ and a _Reservation Length_, the JavsaScript `get_opening_hours` runs and first finds the opening hours for that day, by first checking `ExceptionalOpeningHours` (e.g. if the chosen date is Christmas Day, New Years' Eve, there might be abnormal opening hours). If no entry for that date exists, the relevant weekday entry for `NormalOpeningHours` is retreived. This script is run any time the date or length are changed. The earliest available reservation time is that day's opening time, and the latest is exactly the closing time, minus the reservation length. For example, if the restaurant is open from 10:00 - 21:00, and your reservation length is 1.5 hours, you will be able to book a table (in 15 minute intervals) from 10:00 to 19:30.

![Make A Reservation](/media/readme-images/make_a_reservation.png)

- Once the user has entered their desired reservation details (and after data validation has asked them to correct any invalid inputs), they click _Check Availability_ and the available tables (as described in the flowchart above) are displayed, with a map of the restaurant directly under. 

![Available Tables](/media/readme-images/available_tables.png)

![Table Layout](/media/readme-images/table_layout.png)

- If no such tables are available, or if the user requests a booking for a group larger than any of the tables can accommodate, a link apppears, that sends the user directly to the _Contact_ form.

![Large party booking form](/media/readme-images/large_party_booking_form.png)

![Large party alert message](/media/readme-images/large_party_alert_message.png)

- The contact details of the user are prepopulated, the message from the reservation is fetched, and the subject line of the email is a summary of the requested reservation. The user can then add/edit the message, and send it directly to the restaurant.

![LArge party contact form](/media/readme-images/large_party_contact_form.png)

- In the case of a smaller patry size, if the user's search returns one or more avaiable tables, they can choose which one to book. In this example, the user chooses table 41.

![Select available table](/media/readme-images/select_available_table.png)

- When they click _Reserve Table_, a confirmation page appears.

![Reservation Creation Confirmation](/media/readme-images/reservation_creation_confirmation.png)

- Simultaneously, 2 emails are generated: one for the user, and one for restaurant. (Note: all sensitive information (email password, app password, as well as database information) are stored in an `env.py` file, and/or the Heroku Configuration Variables).

![Reservation Creation Email Guest](/media/readme-images/reservation_creation_guest.png)

![Reservation Creation Email Restaurant](/media/readme-images/reservation_creation_restaurant.png)

- If the user wishes to edit their reservation, they can (if signed in) click on _My Reservations_. Here, a table populated with the user's reservation details appears. Here, the newly made reservation for 22/10/2024 can be seen.

![My Reservations original](/media/readme-images/my_reservations_before.png)

- When the user clicks on _Edit_, they are redirected to the _Edit My Reservation_ form, where the booking information (including the message, if any) is included. The user can then change their reservation information.

In this example, the user has moved the reservation to 30 minutes earlier, made it 30 minutes longer, and they have added an extra message.

![Change to reservation](/media/readme-images/changes_to_reservation.png)

- When the user clicks on _Check Availability_, the same logic as before happens, with 1 noticable difference: the current reservation that the user is editing, is excluded from the list of reservations that are compared to the potential new one. This means that in this instance (and similar instances), the user's original table is shown as being available, because if they are editing their reservation, the original timeslot will not exist (note: the reservation entry remains, but the time is changed). 

![Edit Reservation Available Tables](/media/readme-images/available_tables_edit.png)

- However, in this case (for the sake of being able to see the changes in _My Reservaitons_), the user has decided to change to table 12. When they click on _Update Reservation_, a confirmation page appears.

![Reservation Update Confirmation](/media/readme-images/reservation_update_confirmation.png)

- Simultaneously, 2 emails are generated: one for the user, and one for restaurant. Both the original reservation's details, and the new reservation's details are included in the email.

![Reservation Updated Email Guest](/media/readme-images/reservation_updated_guest.png)

![Reservation Updated Email Restaurant](/media/readme-images/reservation_updated_restaurant.png)

- The changes to the reservation can be seen in _My Reservations_. 

![My Reservation Updated](/media/readme-images/my_reservations_original.png)

- If the user wishes to cancel their reservation, they can simply click on _Cancel_. A warning page comes up, in order to confirm that the guest does indeed wish to delete their reservation.

![Cancel Reservation Check](/media/readme-images/cancel_reservation_confirm.png)

- If the user clicks _Yes, Cancel_, the corresponding entry from the database is deleted and a confirmation message appears.

![Cancel Reservation Confirmed](/media/readme-images/cancel_reservation_confirm_2.png)

- Simultaneously, 2 emails are generated: one for the user, and one for restaurant. The reservation details are sent to the restaurant, and a heartfelt message is sent to the user.

![Reservation Cancelled Guest](/media/readme-images/reservation_cancelled_guest.png)

![Reservation Cancelled Restaurant](/media/readme-images/reservation_cancelled_restaurant.png)

- The reservation is no longer seen in _My Reservations_.

![My Reservations deleted](/media/readme-images/my_reservations_after.png)

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
3. Go to the **Settings** tab, click on **Reveal Config Vars**.
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

  ![Chosen allergens reset](/media/readme-images/bug_filter_choices_lost_2.png)

  When a user navigated to the enlarged image and information of a menu item and then clicked _Back to Menu_, the chosen allergens/dietary requirements were erased, meaning they needed to be selected again.

  The solution to this was to store the chosen allergens in the url of both the main menu page, but also the detailed image/information page, meaning that the allergen/dietary requirement information could eaily be passed back and forth, meaning the user would not hav to re-input their choices.

  ![Chosen allergens stored](/media/readme-images/bug_filter_choices_lost_1.png)

- **Heroku App crashes after running `pip3 freeze > requirements.txt`**

  This occured a couple of times. After comparing the `requirements.txt` files on GitHub, I saw that the module `python-dateutil` was being removed when I ran the command. This may have been due to the virtual environment I was writing code in. Adding it manually to `requirements.txt` fixed this issue.

- **Booking Form data lost when _Check Availability_ was being clicked**

  The reason for this was the I originally had the _Available Tables_ (as well as the vooking form) load in a new url. This meant that (without adding a way of requesting the data from the previous page) the later page lost the booking information, and could therefore not read the data from the form it was supposed to use to calculate the available tables.

  ![Form Information Lost](/media/readme-images/bug_form_data_lost_when_check_availability_1.png)

  I fixed this by embedding the _Check Availability_ function in the same url page (and HTML file) as the _Make a Reservation_ form (and later the _Edit Reservation_ form). This fixed the issue.

  ![Form Information No Longer Lost](/media/readme-images/bug_form_data_lost_when_check_availability_2.png)

- **Mandatory Opening and Closing times, even when closed**

  When I tried added an entry to the `ExceptionalOpeningHours` database (e.g. that the restaurant is closed on Christmas Day), an error appeared stating that I had to add an opening and closing time.

  ![Error when restaurant closed on special day](/media/readme-images/bug_missing_times_when_is_open_false_1.png)

  This was due to the definition of these attributes in my model.

  ![Previous ExceptionalOpeningHours model](/media/readme-images/bug_missing_times_when_is_open_false_2.png)

  After adding `null=True, blank=True` to the model, this fixed this issue, as it allowed me to leave these values blank in the case of a day when the restaurant was closed.

  ![New ExceptionalOpeningHours model](/media/readme-images/bug_missing_times_when_is_open_false_3.png)

- **Different formats of date and time**

  I encountered problems when calculating `reservation_end_time`, due to `reservation_start_time` and `reservation_length` being in two different formats. A single line to convert them to the same type was enough to fix the problem.

- **Opening Hours not being fetched in footer**

  Originally, I could not get the opening hours to load in the footer.

  ![Opening Hours Not Loading](/media/readme-images/bug_opening_hours_not_fetched_footer_1.png)

  [After doing some reaserach](https://docs.djangoproject.com/en/5.0/ref/templates/api/#:~:text=context_processors%20is%20a%20list%20of,be%20merged%20into%20the%20context.), I realised I needed a context processor, as I wanted to fetch information without having to call a function.

  ![Context Processor](/media/readme-images/bug_opening_hours_not_fetched_footer_2.png)

  After creating this simple file and updating the `settings.py` accordingly, the problem was resolved.


- **Changing an opening time reorders the days in the footer**

  When I was testing the updating of opening hours in the footer, I noticed that if I edited a day, it went to the end of the list.

  ![Days reordering after editing](/media/readme-images/bug_days_reordered_after_change.png)

  I initially tried ordering by `day`, but this ended up ordering them in alphabetical order (possibly due to `DAY_CHOICES` being unordered).

  ![Days reordering alphaetically](/media/readme-images/bug_days_reordered_alphabetically.png)

  I solved this by attaching a numberical value to each day in the context processor, ensuring that no matter what order the information was fetched from the database, the result would be displayed from Monday to Sunday.

  ![Days correctly ordered](/media/readme-images/bug_days_correct_order.png)

- **Error 404 for tables sizes of 0 or >50**

  Whilst testing, I noticed that entering 0 or above 50 as the number fo guest led to an error 404, even when `DEBUG` was set to `true`. After checking the code, I found that I had included errors with the form, but I had (at an earlier point in development) added the following lines, possibly to try and catch errors:

  ![Number of guests bug cause](/media/readme-images/bug_number_of_guets_cause.png)

  After deleting this line, the relevant error messages appeared when such a value was entered in the form.

  ![Number of guests 0 error message](/media/readme-images/bug_number_of_guests_zero.png)

  ![Number of guests over 50 error message](/media/readme-images/bug_number_of_guests_over_50.png)

  ![Number of guests error message](/media/readme-images/bug_number_of_guests_error_message.png)

- **HTML Validation Error**

  Whilst doing HTML validation, I repeatedly encountered this error on the booking forms:

  ![HTML Validation Error](/media/readme-images/html_validation_error.png)

  This was due to the fact that the JS script that populates the Reservation Time options was only running once the date and reservation length were chosen/changed. This meant that upon loading, it was blank. The way I fixed this was just by adding a default value.

  ![HTML Validation Error Fixed](/media/readme-images/html_validation_error_fix.png)

- **Incorrect Reservation Length being added to reservation**

  When making a reservation, those I tested that were 1.5 or 2.5 hours long, were both being saved as 2 hours long. Since this was a problem only for the decimal values of hours, I figured it was to do with a possible float/integer mix up. It was in fact due to the float being rounded in my calculations of the reservation end time that led to the mistake.

  ![Float rounding error before](/media/readme-images/bug_float_round_error_before.png)

  After reading more about the timedelta function, I read that it can handle floats as inputs to the number of hours, minutes etc. This led to the following as a more elegant and understandable solution:

  ![Float rounding error after](/media/readme-images/bug_float_round_error_after.png)


### Unresolved

- When the user clicks on a reservation to edit on their _My Reservations_ page, the data from their reservation loads into the form. However, the time slot instead loads to the last chosen time slot. This is due to the JavaScript overwriting the imported data. After many attempts at rewriting the JaveScript code, I couldn't come up with an elegant solution. It is a minor inconvenience, and a slighlty under-functioning extra, so I don't consider it to be a major issue.

## Testing & Validation

### Manual Functional Testing

Below are the records for the manual testing of all functionalities of the application.

**Navbar**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|
|BigByte logo|Click|Homepage loads|PASS|
|Home|Click|Homepage loads|PASS|
|Make a Reservation|Click, whilst logged in|Reservation form appears, with user information prepopulated in First Name, Last Name and Email|PASS|
|Make a Reservation|Click, whilst NOT logged in|Sign In page appears, asking the user to sign up or sign in|PASS|
|See our Menu|Click|Menu and filters appear|PASS|
|My Reservations|Is it visble whilst logged in?|YES|PASS|
|Sign Up|Is it visble whilst NOT logged in?|NO|PASS|
||Is it visible whilst logged in?|NO|PASS|
||Is it visible whilst NOT logged in?|YES|PASS|
||Click|Sign up page appears, asking the user to enter their email and create a secure password|PASS|
|Sign In|Is it visible whilst logged in?|NO|PASS|
||Is it visible whilst NOT logged in?|YES|PASS|
||Click|User is asked to enter their existing user info and log in. When logged in, Navbar is updated to show My Reservations, and Sign Up and Sign In are replaced with Sign Out|PASS|
|Sign Out|Is it visible whilst logged in?|YES|PASS|
||Is it visible whilst NOT logged in?|NO|PASS|
||Click|User is asked for confirmation. When clicked, user is signed out. Navbar is updated to no longer show My Reservation, and Sign Out is replaces with Sign Up and Sign In|PASS|


**Footer**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|
|Email link|Click|Contact Form opens, prepoulated if user is logged in|PASS|
|Opening Hours|Change data in database|New times are shown upon page reload|PASS|
|Facebook|Click on logo|Facebook opens in a new tab|PASS|
|Instagram|Click on logo|Instagram opens in a new tab|PASS|
|GitHub|Click on logo|My GitHub profile opens in a new tab|PASS|
|LinkedIn|Click on logo|My LinkedIn profile opens in a new tab|PASS|


**Booking Form (Make a Reservation and Edit Reservation)**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|
|Reservation Date calendar widget|Click|Calendar opens with todays date as the default. Any day from todays date to 1 year in the future can be chosen. If an invalid date is written in manually, clicking Check Availabilty will not work, it will instead scroll up back to the date field to highlight the mistake|PASS|
|Reservation Length select field|Click arrow at side of drop down box|Selections of 1, 1.5, 2, 2.5 and 3 hours appear. Manual input is not possible|PASS|
|Reservation Time options field|Change Reservation Date and/or Reservation Length|Once the change to length/date is made, the js script is executed and populates only the feasible times based on the opening hours for that day and the reservation length|PASS|
|Number of Guests field|Type number of guests|Only numbers are accepted/read in this field, letters/symbols do not appear if typed. If 0 or anything larger than 50 is entered, an error message appears under the field once Check Availability it clicked|PASS|
|Tabe Location selection field|Click arrow at side of drop down box|The options Inside and Outside appear, with Inside the default. Manual input is not possible|PASS|
|Message field|Type|Anything typed is mirrored in the message box. The markings on the bottom right corner allow for the box to be enlarged if necessary|PASS|
|Booking Form is missing any of the above entry fields (excluding Message, which is optional)|Click Check Availablility|An error message appears under the relevant field, highlighting the cause of the error. The page scrolls up to show this error more clearly|PASS|
|Booking Form has entries for all fields, but Reservation Date has been manually written as a date outside of the next calendar year|Click Check Availability|The error is highlighted and the page scrolls up|PASS|
|Number of Guests field|A negative number is entered, then click Check Availability|An error message explains that the value must be greater than 0|PASS|
||0 is entered, then click Check Availability|An error message explains that the value must be between 1 and 50|PASS|
||A number greater than 50 is entered (e.g. 60), then click Check Availability|An error message explains that the value must be between 1 and 50|PASS|
||A number larger than the largest table size is entered, but less than 50 (e.g. 20)|The following appears: _"If you wish to book a table for 20 people, please contact us using the contact form"_. The second half of the message is a clickable link to a prepopulated contact form|PASS|
|Check Availability response|Valid information is entered, but no matching tables are available|The following appears: _"Unfortunately, we do not have a table available for your group of X at the chosen time. Please contact us using the contact form for assistance, or try searching for another time or date"_, where X is replaced by the number of guests entered in the form. The second half of the message is clickable and again leads to a prepopulated contact form|PASS|
||Valid information is entered and one or more tables are available|A list of all of the smallest tables that match the booking's requests are shown, each with an active _Reserve Table_ button in the case of making a reservation, and _Update Reservation_ in the case of editing a reservation|PASS|
|Reserve Table/Update Reservation buttons|Click|Thank you page opens. A confirmation email is sent to both the restaurant and the guest with the reservation details. In the case of an updated reservation, the email contains both the old and new reservation information|PASS|


**My Reservations**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|
|List of current reservations|Do the shown reservations accurately reflect the data in the database?|YES|PASS|
|Edit button|Click|Edit Reservation form opens, with information prepopulated. [See note in Unresolved Bugs](#unresolved)|PASS|
|Cancel button|Click|User is asked if they wish to cancel|PASS|
|Yes, Cancel button|Click|Reservation is deleted from the database. The restaurant and the user both get an email confirming this|PASS|


**See our Menu**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|
|Filter button|Click|Chosen allergens/preferences are applied to the search|PASS|
|Clear Filters button|Click|All chosen allergens/preferences are unchecked|PASS|
|Gluten|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Crustaceans|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Eggs|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Fish|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Peanuts|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Soy|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Dairy|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Nuts|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Celery|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Mustard|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Sesame|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Sulphites|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Lupin|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Molluscs|Check box, click filter|All items from the menu including this allergen (and any other checked allergens/preferences) are removed from the displayed items|PASS|
|Vegan|Check box, click filter|All items from the menu that are NOT vegan are removed from the displayed items|PASS|
|Vegetarian|Check box, click filter|All items from the menu that are NOT vegetarian are removed from the displayed items|PASS|
|Menu item title|Click|Larger image and description opens in the same tab. The url name/slug is the name of the dish|PASS|
|Menu item image|Click|Larger image and description opens in the same tab. The url name/slug is the name of the dish|PASS|
|Back to Menu (under larger image)|Click|Return to menu, with previously chosen checkboxes still checked and applied|PASS|
|Make a Reservation (under larger image)|Click when logged in|Redirected to Make a Reservation page, user information prepopulated|PASS|
|Make a Reservation (under larger image)|Click when NOT logged in|Redirected to Sign Up page|PASS|


**Contact Us**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|
|Contact Form in navbar|Click whilst user is logged in|Contact Form page loads, users information (First Name, Last Name, Email) is prepopulated, but can be altered|PASS|
||Click whilst user is NOT logged in|Unpopulated contact form loads|PASS|
|Contact Form - Large group, redirected from Make a Reservation/Edit Reservation|Attempt to make a reservation for a large group (e.g. 20). Click on link that appears|Information entered in reservation form populated in contact form's subject line. Message from reservation form (if non-empty) populated into message field|PASS|
|Contact Form - No available table, redirected from Make a Reservation/Edit Reservation|Attempt to make/edit a reservation for a time when there are no available, feasible tables. Click on link that appears|Information entered in reservation form populated in contact form's subject line. Message from reservation form (if non-empty) populated into message field|PASS|


**Sign In, Sign Out, Sign up**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|
|Sign In function|Enter an invalid email/password combination|The following appears: _"The email address and/or password you specified are not correct"_. Status remains NOT signed in|PASS|
||Enter a valid user (non superuser) email/password combination|The user is signed in. The _My Reservations_ link appears in the navbar. The _Sign In_ and _Sign Up_ links in the navbar become a _Sign Out_ link, reflecting the fact that the user is logged in. Their contact info is prepopulated into the contact form and booking form upon opening. They are unable to access the Django admin panel|PASS|
||Enter a valid superuser email/password combination|The user is signed in. The _My Reservations_ link appears in the navbar. The _Sign In_ and _Sign Up_ links in the navbar become a _Sign Out_ link, reflecting the fact that the user is logged in. Their contact info is prepopulated into the contact form and booking form upon opening. They are able to access the Django admin panel|PASS|
|Sign Up function|Enter an invalid email|An error message appears, not allowing the user to create an account with an invalid email|PASS|
||Enter an invalid password (e.g. too short, using a common word)|An error message appears, reflecting the issue with the password|PASS|
||Enter a valid email/name/password combination|A new user account is added to the Django database. The user is automatically signed in|PASS|
|Sign Out function|Click _Sign Out_|A confirmation message appears, checking that the user in fact wants to sign out|PASS|
||Click and confirm _Sign Out_|The user is signed out. The _My Reservations_ link disappears from the navbar. The _Sign In_ and _Sign Up_ links appear in the navbar, whilst the _Sign Out_ link disappears, reflecting the fact that the user is not logged in. Their contact info is no longer prepopulated into the contact form and booking form upon opening|PASS|
||Click any other link on the site, or back|The user remains signed in|PASS|


**Error Pages**

|Test Item|Test Carried Out|Result|Pass/Fail|
|-------------|------------------|-----------|-------|
|404 Error|Force a 404 error by adding `/doesnotexist` to url|404.html loads with link to Home page|PASS|
|500 Error|Force a 500 error by removing `ALLOWED_HOST` from `settings.py`|500.html loads with link to Home page|PASS|

I was unable to find a reliable way to test the 400 and 403 error pages. However, [after reading about default template names in Django's documentation](https://docs.djangoproject.com/en/5.0/ref/views/), coupled with the fact that the 404 and 500 error pages work, I am confident that they will also work.

### Automated Testing

For this, I used the inbuilt testing module `unittest`. I tested the `menu_item_list` view in the _Allergens_ app. This is the view that controls the filtering of dishes containing certain allergens and whether they are vegan/vegetarian.

In order for this test to pass, the view needs to do the following:

- FAIL if any of the inputs are not `Boolean`. The input into this function is a series of Boolean values stating whether certain allergens/dietary requirements apply or do not apply.
- FAIL if any of the inputs are of the type `None`, i.e. there is missing data. In order for the function to be accurate, an input must be received for each of the dietary criteria.
- If the input for an allergen **a** is `True`, then the return **must not** include any entries from the _MenuItem_ database that have the attribute `a` value set to `True`.
- If the input for an allergen **b** is `False`, then the return must not exclude any entries from the _MenuItem_ database based on their `b` value. For example, if you do **not** have a _Peanut_ allergy, then the item's **Peanut** variable value is irrelevant; it must not affect the return. 
- If the input for **Vegetarian** is `True`, then the return **must not** include any entries from the _MenuItem_ database that have the attribute `vegetarian` value set to `False`.
- If the input for **Vegetarian** is `False`, then the return must not exclude any entries from the _MenuItem_ database based on their `vegetarian` value. If you are not a vegetarian, then the item's **Vegetarian** variable value is irrelevant; it must not affect the return. 
- If the input for **Vegan** is `True`, then the return **must not** include any entries from the _MenuItem_ database that have the attribute `vegan` value set to `False`.
- If the input for **Vegan** is `False`, then the return must not exclude any entries from the _MenuItem_ database based on their `vegan` value. If you are not a vegan, then the item's **Vegan** variable value is irrelevant; it must not affect the return.

Whilst testing, one of my tests (`test_dietary_requirement_not_ticked_filtering`) failed repeatedly.

![Test Fail](/media/readme-images/test_fail_2.png)

After examining it further, the reason that it failed is due to the way the information is being passed. Since `default=True` for all of the allergen/dietary variables, they are simply not included in the url, if they are not selected. Hence, my search for `'?vegan=false'` could not exist in the actual application of the view `menu_list_item`. The way I solved this issue was to change the approach taken by the test. After ensuring the test included both `vegan=True` and `vegan=False` values, I simply checked that not applying the `vegan` filter resulted in both vegan and non-vegan dishes being included in the response. The test passed.

### PageSpeed Testing

The website receieves high score on all pages. I have attached 2 images from PageSpeed testing that represent the scores that the website received. As there are a lot of different parts to the website, I have only included 2.

![PageSpeed Result - Home](/media/readme-images/pagespeed_home.png)

![PageSpeed Result - Allergens](/media/readme-images/pagespeed_allergens.png)

### WAVE Testing

Web Accessibility Evaluation Tools revealed 0 errors.

![WAVE Result](/media/readme-images/wave_result.png)

![WAVE Alerts](/media/readme-images/wave_alerts.png)

The 2 alerts are for the following:

- Skipped heading level: on some pages, there may be `<h1>` tags and `<h3>` tags, but no `<h2>` tags. Since this is part of the styling I have chosen, this is of no concern.
- _Home_ appears in the navbar, even when on the _Home_ page. This is by choice, for consistency in the styling and appearance of the navbar.

### HTML

All locations on the site passed HTML validation with no errors. Due to the large number of individual HTML pages/templates that are used, below are a few examples of test results.

![HTML Validation - Home](/media/readme-images/html_pass_home.png)

![HTML Validation - Current Reservations](/media/readme-images/html_pass_current_reservations.png)

![HTML Validation - Checked Allergens Menu](/media/readme-images/html_check_allergens_menu.png)

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

__allergens/test.py__

![Python Validation allergens/test.py](/media/readme-images/lint_allergens_test.png)

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

__booking/urls.py__

![Python Validation booking/urls.py](/media/readme-images/lint_booking_urls.png)

__booking/views.py__

![Python Validation booking/views.py](/media/readme-images/lint_booking_views.png)


## Future Improvements/Developments

- Add possibility for user to select several tables when booking for a larger group. Although the current logic (directing the user to the contact form) deals with this instance (and is arguably better and more flexible from the restaurant's point of view), I feel this would be a nice touch, and would give larger parties even more control over their dining experience.
- Cascade for when the opening hours are changed, affecting an already existing reservation. If, for example, the restaurant decides to begin closing early on Mondays or they decide to add an extra day to `ExceptionalClosingHours`, ideally a message should be sent to all future guests that have a reservation affected by this alteration (as well as to the restaurant to notify them of this). The current workaround would be to filter the existing reservations on the Django Admin panel and manually contact them (which is standard practise in most places), but an automated response would be more professional.
- Add logic to the _MenuItem_ database, so that any item with _Dairy_ or _Eggs_ set to `True`, automatically has _Vegan_ set to `False`. This should not be an issue if data is input correctly, but it gives the user less chance to introduce an error/inconsistency into the model.
- Assuming this was a real restaurant, I would hire a professional photographer to take real photos of the food, as opposed to [using manually generated images](#technology--resources).
- Add an email/SMS reminder 24 hours before a booking to remind a guest of their reservation.

## Acknowledgments

- **Student Care**: Quick responses and troubleshooting, especially when there were issues with the CI Database.
- **Mentor**: Having the ability to find broken logic and quickly point out areas that need improving.
