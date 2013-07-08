import webapp2



class MainPage(webapp2.RequestHandler):
    
    
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write('Hello, webapp World!')
        questions=["1. I can easily recognize practical needs and I'm quick to meet them.", '2. I give to support and bless others or to advance an effective Ministry.', '3. I will discontinue personal counseling if no effort to change is seen.', '4. I am attracted to people who are hurting or in distress.', '5. I quickly and accurately identify good and evil and hate evil.', '6. I usually solve problems by first applying scriptural principles.', '7. I want to clear up problems with others quickly.', '8. I enjoy working with and being around people, the more the better.', '9. I especially enjoy manual projects, jobs, and functions.', '10. I have a strong belief in tithing (10% of income) and in giving in addition to tithing.', "11. I desire above all else to see God's plan worked out in all situations.", '12. I keep everything in meticulous order.', "13. It's OK to use Scriptures out of context in order to make a point.", "14. I'm constantly writing notes to myself and making lists of things to do.", "15. I encourage repentance that produces positive change in a person's life.", '16. I almost always look for the good in people and tend to overlook their faults.', '17. I have strong convictions and opinions based on my investigation of facts.', '18. I like to get the best value for the money I spend and often bargainhunt.', '19. I am a detail person with a good memory.', '20. I especially enjoy working with long-range goals and projects', '21. I easily detect insincerity or wrong motives in others.', '22. I especially enjoy showing hospitality.', "23. I'm a natural and capable leader and often in leadership positions.", "24. I'm often intolerant of opinions and views that differ from my own.", '25. I am quick to volunteer whenever I see a need for help.', '26. I often grieve deeply over the sins of others.', '27. I rejoice to see other blessed and grieve to see others hurt.', '28. I will stay with something until it is completed.', "29. I'm willing to let others get the credit in order to get a job done.", '30. Things are either right or wrong; there really are no indefinite areas.', "31. I'm always encouraging others to develop in their personal ministries.", '32. I have natural and effective business ability.', "33. I'm a crusader for good causes.", '34. I have a hard time saying no to requests for help.', '35. I prefer to move on to a new challenge once something is completed.', '36. I view trials as opportunities for personal growth to be produced.', '37. I know I am definitely called to intercession(praying for others).', '38. I take action to remove hurts and relieve distress in others.', '39. I am more interested in meeting the needs of others than my own needs.', '40. The Bible is the only basis for truth, belief, action, and authority.', '41. Because giving is so important, I tend to pressure others to give.', '42. I realize I have a tremendous capacity to show love.', '43. I enjoy working on immediate goals rather than long-range goals.', '44. I can easily tend to drive myself and neglect personal and family needs.', '45. I make decisions easily.', '46. I am eager to see my own blind spots and help others see theirs too.', "47. I'm delighted when my gift is an answer to someone' s specific prayer.", '48. I like to check out the source of information that others present.', '49. My greatest fulfillment is in working to accomplish goals.', '50. I desire to be obedient to God at all costs.', '51. I absolutely love to encourage others to live victoriously.', '52. I expect a lot of others and myself.', '53. I realize that I need to feel appreciated.', '54. I easily sense the spiritual and emotional atmosphere of a group or individual.', '55. I give freely of my money, possessions, time, energy, and love to others.', '56. I enjoy delegating tasks and supervising people.', '57. I get upset when Scripture is used out of context.', "58. I tend to do more than I'm asked to do.", '59. I love to do thoughtful things for others.', '60. I love to study and do research.', '61. I tend to be judgmental and blunt.', '62. My greatest joy is in doing something that is helpful.', '63. I am constantly promoting the spiritual growth of groups and individuals.', '64. I do not want to lead others. ', '65. I sometimes use financial giving to get out of other responsibilities.', "66. I'm more concerned for mental and emotional distress than physical distress.", '67. I believe the acceptance of difficulties will produce positive results.', '68. I avoid conflicts and confrontations.', '69. My family and friends can get upset with my unpredictable patterns of giving.', '70. I always complete what I start.', '71. I know when to keep old methods going and when to try new ones.', '72. I love to give quietly, without others knowing about it.', '73. I express ideas and organization in ways that communicate clearly.', '74. I am emotionally self-controlled.', '75. I am intellectually sharp.', '76. I believe God is the Source of my supply.', '77. I am slow to accept viewpoints of others unless they can prove they are right.', '78. I prefer to apply truth rather than to research it.', '79. I find truth in experience first, and then confirm it with scripture.', '80. I am especially good at supporting others who are in leadership.', '81. I am very fluent in communication.', '82. I will assume responsibility where no specific leadership exists.', '83. I love to do personal counseling.', '84. I often intercede (pray for) for the hurts and problems of others. ', '85. I easily perceive the character of individuals and groups.', '86. I have the ability to handle my own finances with wisdom and frugality.', "87. I can easily neglect my own family's needs by being too busy helping others.", '88. I always present truth in a logical, systematic way.', '89. I like to confirm truth by checking out the facts.', "90. I realize I'm pushy in trying to get others and groups to mature spiritually.", '91. I realize that I tend to be ruled by my heart rather than my head.', '92. I prefer teaching believers to engaging in evangelism.', "93. I have great zeal and enthusiasm for whatever I'm involved in.", '94. I feel that absolute truth must always be established even if it hurts.', "95. I'm willing to endure criticism in order to accomplish the ultimate task.", "96. I'm drawn to others with the gift of compassion.", '97. I accept people where they are without judging them.', '98. I get involved in hospitality because it is an opportunity to give.', '99. I like to emphasize facts and the accuracy of words.', "100. I'm careful with my words and actions to avoid hurting others.", '101. I prefer to use biblical illustrations rather than life illustrations.', "102. I'm highly motivated to organize that for which I'm responsible.", "103. I want a visible response from people when I'm teaching or speaking.", '104. I regularly intercede for needs and the salvation of souls.', '105. I feel Bible study is foundational to everything in life.']
        self.response.out.write('''
        <html>
            <head>
                <title>
                spiritual gifts assessment test change
                </title>
            </head>
            <body>
            <form action ="/submit" method=post> 
            <table width=600>
            <tr><td>this has been true in my life...</td><td>most of the time<br />4</td><td>often<br />3</td><td>sometimes<br />2</td><td>seldom<br />1</td><td>not at all<br />0</td></tr>
        ''')
        for question in range(len(questions)):
            self.response.out.write('<tr><td>'+questions[question]+'</td>')
            for x in range(5):
                self.response.out.write('<td><input type="radio" value="'+str(4-x)+'" name="question'+str(question)+'" /></td>')
            self.response.out.write('</tr>\n')
        self.response.out.write('</table></form></body></html>')
        
class evaluator(webapp2.RequestHandler):
    
    def post(self):
        pass
        


application = webapp2.WSGIApplication([('/', MainPage)], debug=True)

def main():
    application.run()

if __name__ == "__main__":
    main()