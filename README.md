# GRAPHICS BY TOM

Graphics by Tom is a site that allows someone who works freelance and needs a website (in this case Tom)
to be able to save time by having everything in the same place for both the site host and for the site users.
It clearly shows everything a freelance worker would need to display to clients while also being the hub for
their work and the work they need to achive!

## UX

The UX for this site revolved around the fact that the users were coming here for information while the host was
here for work. This meant the site had to look professional and clean while still serving as a perfectly functioning
site for the two purposes.

### user stories

- As someone who reguarly hires graphics designers I need to be able to see the work quickly and simply to gauge if your style is what we need.
- As a graphics designer I would love to be able to have both my CV and my current work all in one place!
- As somebody who is new to this field, I would like a clearly labled site so I know what im looking at and getting.

I believe that Graphics by Tom meets all of these users preferences.

### display testing

The /wireframes file will show two templates of how I planned the site, little has changed but I changed what was needed.
.....

## Features

- Viewing the designers previous work, this is done by clicking 'Previous work' on the home page.
- Ordering/paying for work from the designer, this is done by clicking 'Ordering work' and filling out a simple form that takes
you to a payment form where you can then pay for your order.
- Editing and adding previous work, this is done by the site admin who can go onto the previous work page and then add/edit
selected pieces of work and their information.
- Deleting a piece, this is doen two ways which are either the admin marking a order as complete or the admin deleting a post on the previous
work page via the 'delete' button.
- Filtering work on the previous work page, this is done on the page but simply clicking what catagory you would like to 
filter by at the top of the page and you are able to click clear to reverse this step also.

### Future features

- I would set up a session storage system, with this the unpaid for orders would not sit in a void in the database as they currently
do but would instead not exist unless they were purchased.
- More complex filter, I believe the filter I have inplace works perfectly for what it needs to do, however doen the line
if the number of items on the previous work page are very large then multiple may be required to refine your search clearly.

## Technologies used

- HTML5
    - My templates are forms were all written using html.
- CSS3
    - My site was styled using css.
- JavaScript
    - My site used javascript to implement Stripe and improve UX.
- Django 
    - Django was used to in my site for database purposes and to connect everything together.
- Bootstrap
    - Provides documentation templates for html and css.
- MySOL + Postgres
    - These were used for databases for my develpment and deployment code.


## Testing 

My first testing stage was debug set to true. This proves to me that the code syntax was correct and the code ran.
If not the application wouldn't run and I would be able to visually see the errors and as is done by the computer.
This was not only do I know that my code will run, I know it is laid out efficiantly and well.

My edit function specificlly was very greatful for the debug system as I had to import specific IDs of items from the
database that in a language I was fairly new to. This allowed me to make the page to the best of my ability without
any remaining errors.

As much as the debug system worked well for me, the UX had to be tested by eye. This meant I would have to take my user
stories and adapt my site to incorporate them. Here is an example.

- Previous work page:
    1. View previous work and see it listed in a 1 per row format which I diddnt find TO look nice or be efficiant.
    2. Add a 2 by row format which although looked cleaner still looked like a waste of space.
    3. Decided on a 3 row format where I found the pieces display were not too small but not too large.
    4. I then wanted the content inside to display looking organised and neat, this was done by simply letting the 
    text sit on the left of their column.

My site is designed to be clean and sharp on all resolutions, boostrap row feature helped me do this with eas as well as
boostraps form customisation. This prevented the screen from ever looking crowded or scruffy and makes zero impairment whether
youre looking at a huge screen or a tiny one!

## Deployment 

Gitpod was great for letting me preview my work before it was deployed, this helped me get a real understanding of how my site
would look when fully deployed to Heroku. Due to the close relationship of the two sites it made getting one to the other remarkably
straight forward and any errors would display clearly for a quick fix.

##Credit

###Content 

- The template for my nav bar was acquired from bootstrap.
- The format for my payment form was acquired via Stripe.

### Acknowledgements

My inspiration for my site came from the project recomendations. I saw this idea and could almost instantly invision it, I played around with
a few diffrent ideas to see which one I prefered but it always came back to the original. I think this is due to my appriciation for art
and graphics design and my desire to become a freelance worker in the future myself helping fuel me for this project.
