Feature: signup

          as a user 
          I want to create a user
          the user signs up with credentials not registered on the system.

 Scenario: sign up validate pop up 
        Given the user is on https://www.demoblaze.com/
        When the user signs up with credentials not registered on the system.
        Then pop up Sign up successful
       