Feature: login

	as a user
	I want to login
	in order to validate figure the user login name
	
	Scenario: Login with valid credentials
		Given the user is on https://www.demoblaze.com/
		When the user logs in with valid credentials
		Then the name of the user appears on the page
