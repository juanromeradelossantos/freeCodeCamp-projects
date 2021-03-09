
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.neural_network import MLPClassifier


@ignore_warnings(category=ConvergenceWarning)

def player(prev_play, opponent_history=[], opponent_history_nums=[], X_train=[], y_train=[]):

    model = MLPClassifier(
      solver='adam',
      hidden_layer_sizes=(30,),
      learning_rate='constant',
      max_iter=300,
      shuffle=False,
      random_state=55
    )

    if not prev_play:
      prev_play = 'R'
    
    opponent_history.append(prev_play)
    
    letter_to_num = {'R': 0, 'P': 1, 'S': 2}
    opponent_history_nums.append(letter_to_num[opponent_history[-1]])
    
    # featurize: 5 features and 1 label
    if len(opponent_history_nums) >= 6:
        X = opponent_history_nums[-6:-1]
        y = opponent_history_nums[-1]

        X_train.append(X)
        y_train.append(y)

        # use just the last 50 entries to capture changes in play style
        if len(y_train) > 50:
            del X_train[0]
            del y_train[0]

        model.fit(X_train, y_train)

        pred = model.predict([opponent_history_nums[-5:]])

        ideal_response = {0: 'P', 1: 'S', 2: 'R'}
        guess = ideal_response[pred[0]]

    else:
      guess = 'P'

    return guess
