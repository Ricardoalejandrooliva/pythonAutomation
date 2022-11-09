Feature: signup

	as a user
	I want to create a user
	the user signs up with credentials not registered on the system.

	Scenario: sign up validate pop up
		Given el usuario este en la pagina https://www.demoblaze.com/
		When el usuario se registra con credenciales no registradas en el sistema
		Then la pagina muesta el pop up de Sign up successful