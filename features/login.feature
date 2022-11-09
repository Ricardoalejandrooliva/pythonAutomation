Feature: login 

	as a user
	I want to login
	in order to validate figure the user login name
	
	Scenario: Login with valid credentials
		Given el usuario este en la pagina https://www.demoblaze.com/
		When el usuario inicia sesión con credenciales válidas
		Then el nombre del usuario aparece en la página
