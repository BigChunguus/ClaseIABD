#!/usr/bin/python3

from mrjob.job import MRJob
from mrjob.step import MRStep
    
class LaLigaDMR(MRJob):
        
    # Mapper: En esta etapa aún no hay clave (_), el valor lo recibimos en la variable line
    def mapper_goals(self, _, line):
        #Por cada línea, esta se divide en los campos que forman las columnas
        _, _, _, home_team, away_team, home_goals, away_goals, result, *rest = line.split(',')
        
        # Si es la cabecera no emitimos nada
        if home_team == "HomeTeam":
            return

        if result == 'D': 
            yield home_team, (int(home_goals))
            yield away_team,(int(away_goals))
        elif result == 'H':
            yield home_team, (int(home_goals))
            yield away_team,(int(away_goals))
        else:            
            yield away_team, (int(away_goals))
            yield home_team,(int(home_goals))

            
    def combiner_goals(self, team, goals):
        yield team, sum(goals)
            
    def reducer_goals(self, team, goals):
        yield None, (team, sum(goals))
        
    def reducer_goals_classification(self,goals, teams):
        goals= sorted(teams, key=lambda t: t[1], reverse=True)
        goalsFirst = goals[0][0]
        goalsLast = goals[-1][0]
        goalsDiff=goals[0][1]-goals[-1][1]
        
        str_one = goalsFirst + " vs "+ goalsLast
        str_two = "diferencia de goles "+ str(goalsDiff)
        
        yield  (str_one , str_two)
        
    def steps(self):
        return [
            MRStep(mapper=self.mapper_goals,
                   combiner=self.combiner_goals,
                   reducer=self.reducer_goals),
            MRStep(reducer=self.reducer_goals_classification)
        ]

         
if __name__=='__main__':
    LaLigaDMR.run()
