import re

essay = """
Importance of Confusion in William Shakespeare’s The Tragedy of Othello
William Shakespeare’s The Tragedy of Othello reenacts the story of a general who is tricked by his jealous ensign into thinking his newly wed wife is having an affair with his lieutenant. Among with some other defects of this general, it is the confusion Iago, the ensign, creates that is most effective into tricking general Othello of such an absurd situation. Confusion is present throughout the entire play as it moves and drives the plot, many times with egotistical and greedy ends.
Confusion in The Tragedy of Othello emerges from a disparity between expectation and reality, in addition to the lack of communication between characters. More specifically, confusion most frequently appears in the play as Iago gaslights other characters into believing alternate versions of reality which are contrary to these character’s expectations. Confusion is seen from the very first scene, where Iago and Roderigo roused Brabantio and exaggerated Desdemona’s elopement with Othello. Iago suggested to Roderigo:
Call up her father.
Rouse him. Make after him, poison his delight,
Proclaim him in the streets; incense her kinsmen,
And, though he in a fertile climate dwell,
Plague him with flies. Though that his joy be joy,
Yet throw such chances of vexation on ’t
As it may lose some color. (Oth. 1.1.74-80)
Confusion is further foreshadowed during Act II, Scene I, where the storm reduces visibility at the seaport in Cyprus and the protagonist’s ship’s arrival becomes uncertain. In a conversation between Montano and a First Gentleman: “What from the cape can you discern at sea?” which is replied with “Nothing at all. It is a high-wrought flood. / I cannot ’twixt the heaven and the main / Descry a sail.” (Oth. 2.1.1-4) The setting during this scene forebodes how uncertainty and confusion will be present onwards into the play, although can be considered confusion deriving from the ambience. Finally, the epitome of confusion during this play is during the final scene in Act V, scene ii, where confusion, combined with Othello’s hubris, move him to kill Desdemona. Iago’s lies have successfully manipulated Othello into believing Desdemona is unfaithful. However, Desdemona, perplexed and disoriented from Othello’s bizarre accusations, has no response to justify Othello’s confounded sense of reality and dies, although she is innocent.
In many ways confusion emerges in the play to drive the plot. It frequently emerges from Iago’s own actions with the purpose of manipulating others and shaping his own version of reality. One example is how uncertainty and confusion make Brabantio rouse his household in the middle of the night in search for Desdemona, later visiting the Duke of Venice and accuse Othello of witchcraft. (Oth. 1.3.72-75) Confusion here led to impulsiveness and rash actions from Brabantio’s part. Additionally, Desdemona’s loss of the handkerchief, which Iago apparently later finds in Cassio’s household leads Othello to fall in a trance of jealousy and become more gullible for more of the lies Iago keeps feeding him. The actions motivated by these moments of confusion steer the plot and explains Othello's actions in later scenes.
This confusion affects the play, giving characters irrational responses to situations that would otherwise not have happened. Confusion hyperbolizes feelings and actions and fuels drama between characters. A scene that exemplifies this is Othello’s argument with Desdemona over the handkerchief. He asks Desdemona for the handkerchief he gave her as a gift and she cannot give it to him, so he leaves Desdemona in a fit of anger. (Oth. 3.4.59-115) If the handkerchief has such value to Othello, Desdemona would have known about it and would have not reacted with such surprise (Oth. 3.4.80). However, Iago was able to successfully manipulate Othello into confusing the handkerchief’s symbol of love to a symbol of Desdemona’s chastity and purity, greatly exaggerating Othello’s reaction to the loss of a handkerchief. 
All in all, the feeling of confusion bears a critical role in The Tragedy of Othello. It is present throughout the entire play and is primarily presented through Iago. It was even foreshadowed at one point by means of the setting. Its main roles are directed towards the goal of manipulating characters and it affects the play by successfully doing so, and persuading characters to succumb to another’s will.
"""

def frequency(string):
    words = re.split(r'[\n \.]', string)
    freq = dict()
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq
    
freq = frequency(essay.strip().lower())

most_frequent = dict()
order = []

for word, amount in freq.items():
    if bool(word) and amount > 1:
        most_frequent[word] = amount
        order.append((word, amount))
        
order.sort(key=lambda x: x[1])

for word, amount in reversed(order):
    print('({}) {}'.format(amount, word))