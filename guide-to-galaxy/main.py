from src.input_reader import read_sentences
from src.deal_conversion import MerchantRobot

DEFAULT_ANSWER = "I have no idea what you are talking about"


def learn_and_answer(input_file):
    info = read_sentences(input_file)
    error_msgs = info['error_msgs']
    
    if len(info['ref_words']) > 0:
        robot = MerchantRobot(DEFAULT_ANSWER)

        # build the robot's ref words book
        result = robot.learn_knowledge(info['ref_words'], info['price_msgs'])
        if result:
            error_msgs.extend(result)
        
        # use to robot to answer questions
        result = robot.answer_questions(info['questions'])
        if result:
            print("\n".join(result))
        if error_msgs:
            print("\n".join(error_msgs))
    else:
        print("no ref words found")

if __name__ == '__main__':
    
    learn_and_answer('input.txt')