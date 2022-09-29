Feature: signup

          as a user 
          I want to create a user
          in order to validate figure el pop up Sign up successful

 Scenario: sign up validate pop up 
        Given the user is on https://www.demoblaze.com/
        When user must register with non-existing user
        Then pop up Sign up successful