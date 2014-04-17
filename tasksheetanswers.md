#Task sheet 1 questions

##Task 3a questions
1. GetPlayerName()
2. Create a while loop so if the name is invalid the user will be prompted to enter their name again. If the name is valid, it will be returned out the function
3. A variable that continues/ends the while loop, most likely 'valid'. It's data type is boolean. 
Pseudo code for improvements:

FUNCTION GetPlayerName()
	valid: Boolean
	PlayerName: String
	valid <- FALSE
	WHILE valid = FALSE DO
		PlayerName <- INPUT "Please enter your name"
		IF PlayerName = '' THEN
			OUTPUT "You must enter something for your name!"
			valid <- FALSE
		ELSE
			valid <- TRUE
		END IF
	END WHILE	
END FUNCTION

##Task 3b questions
1. UpdateRecentScores()
##Task 5 questions
1. import datetime
2. UpdateRecentScores()
	DisplayRecentScores()
	ResetRecentScores()
	TRecentScore()
3. By using the strptime() function	
	