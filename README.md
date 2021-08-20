# Flask Market
Example of Online-Market with the Flask web framework.

### Instructions:

- Run this command in console: `pip install -r requirements.txt`
- Run the following to set Flask env variables that are necessary
  - `set FLASK_APP=app.py`
  - Run the Project: `flask run` or in console `python app.py`
  
### Additional Info:

- First the visitor will see the home page. Press "Get Started"
- If this the first time visitor visits the website, the visitor shall create the account "Register"

  - There's some limits: username can't be no more than 30 characters but not less than 6; password can be any symbols but no less than 6 symbols.
- Otherwise, "Log in"
  - To see details about items, press "Additional Info"
  - To buy item press "Buy" in next pop-up window press "Buy item" or you'd not like it close the window.
  - To remove bought item from the busket press "Discard" on the card.