Q1="""SELECT AVG(age) FROM Player;"""

Q2="""SELECT match_no,play_date FROM Match WHERE audience > 50000 ORDER BY match_no ASC;"""

Q3="""SELECT team_id,COUNT(win_lose) AS n_won FROM MatchTeamDetails WHERE win_lose='W' GROUP BY team_id ORDER BY n_won DESC,team_id ASC;"""

Q4="""SELECT match_no,play_date FROM Match WHERE stop1_sec > (SELECT AVG(stop1_sec) FROM Match) ORDER BY match_no DESC;"""

Q5="""SELECT mc.match_no,
        t.name as team_name,
        p.name as captain_name
        FROM Team AS t 
            INNER JOIN Player AS p
                ON t.team_id = p.team_id
            INNER JOIN MatchCaptain AS mc
                ON mc.captain = p.player_id
            AND mc.team_id = p.team_id
            ORDER BY mc.match_no ASC,team_name ASC;"""
            
Q6="""SELECT m.match_no,
        p.name,
        p.jersey_no
        FROM Player AS p
        INNER JOIN Match AS m
        ON m.player_of_match = p.player_id
        ORDER BY m.match_no ASC;"""
        
Q7="""SELECT t.name,AVG(p.age)
        FROM Team AS t
        INNER JOIN Player AS p
        ON t.team_id = p.team_id
        GROUP BY t.team_id
        HAVING AVG(p.age) > 26 ORDER BY t.name ASC;"""
        
        
Q8="""SELECT pp.name,
        pp.jersey_no,
        pp.age,
        (SELECT COUNT(gd.goal_id) 
                FROM Player AS p
                        INNER JOIN GoalDetails AS gd
                        ON p.player_id = gd.player_id
                        WHERE p.player_id = pp.player_id
                        )
                AS n_goals
        FROM Player AS pp
        WHERE pp.age <= 27
        GROUP BY pp.player_id
        HAVING n_goals > 0
        ORDER BY n_goals DESC,pp.name ASC;"""
        
Q9="""SELECT team_id,
        COUNT(goal_id)*100.0/(SELECT COUNT(*) FROM GoalDetails)
        from GoalDetails GROUP BY team_id;"""
        
    
Q10="""SELECT COUNT(goal_id)*1.0/COUNT(DISTINCT team_id)*1.0 
        FROM GoalDetails;"""
        
Q11="""SELECT player_id,
        name,
        date_of_birth
        FROM Player 
                WHERE player_id 
                NOT IN
                (SELECT player_id 
                        FROM GoalDetails)
                ORDER BY player_id ASC;"""
        
Q12="""SELECT t.name,
        m.match_no,
        m.audience,
        m.audience -
        (SELECT avg_audience
        FROM
        (SELECT mtd.team_id AS t_id,
                avg(m.audience) AS avg_audience
                FROM MatchTeamDetails AS mtd
                        INNER JOIN Match AS m
                        ON mtd.match_no = m.match_no
                        GROUP BY mtd.team_id)
               WHERE t_id = t.team_id)
        FROM Team AS t
        INNER JOIN MatchTeamDetails AS mtd
        ON t.team_id = mtd.team_id
        INNER JOIN Match AS m
        ON m.match_no = mtd.match_no
        ORDER BY m.match_no ASC;"""