﻿def Schooldata():

    SchoolData=list()
    SchoolData=[
        ["division","very good","good","so-so","bad","very bad"],
        ["Training content",13.1, 37.1, 39.6, 8.7, 1.5],
        ["Training Methods",10.6, 34.6, 39.5, 13.4, 1.9],
        ["friendships",27.1, 40.0, 28.5, 2.9, 1.5],
        ["Relation with teacher",16.2, 37.8, 38.4, 6.8, 0.8],
        ["School Facilities",11.4, 29.8, 39.0, 14.8, 4.9],
        ["School environment",12.2, 26.5, 42.0, 14.9, 4.4],
        ["specialism",13.5, 29.7, 43.4, 11.1, 2.4],
        ["school life",13.7, 37.6, 43.3, 4.1, 1.2]
        ]
 
    data=SchoolData[1:]

    for i in range(0,len(data)):
        print "average of very good and good :",str((data[i][1]+data[i][2])/2)
        print "average of vert bad and bad:",str((data[i][4]+data[i][5])/2)


def Speech1():
    doc=speech1
    d=dict()
    for line in doc:
        words=line.split()
        for c in words:
            if c not in d:
                d[c]=1
            else:
                d[c]=d[c]+1
    c=15
    for k in d:
        if d[k]>c:
            print "speech1:",k
   
    
def Speech2():
    doc=speech2
    d1=dict()
    for line in doc:
        words=line.split()
        for c in words:
            if c not in d1:
                d1[c]=1
            else:
                d1[c]=d1[c]+1
    c=1
    for k1 in d1:
        if d1[k1]>c:
            print "speech2:",k1

            
def lab10():

    Schooldata()
    
    speech1=list()
    speech1=["Fellow-Citizens of the Senate and of the House of Representatives",
    "AMONG the vicissitudes incident to life no event could have filled me with greater anxieties than that of which the notification was transmitted by your order, and received on the 14th day of the present month ",
    "On the one hand, I was summoned by my country, whose voice I can never hear but with veneration and love, from a retreat which I had chosen with the fondest predilection, and, in my flattering hopes, with an immutable decision, as the asylum of my declining years - a retreat which was rendered every day more necessary as well as more dear to me by the addition of habit to inclination, and of frequent interruptions in my health to the gradual waste committed on it by time",
    "On the other hand, the magnitude and difficulty of the trust to which the voice of my country called me, being sufficient to awaken in the wisest and most experienced of her citizens a distrustful scrutiny into his qualifications, could not but overwhelm with despondence one who (inheriting inferior endowments from nature and unpracticed in the duties of civil administration) ought to be peculiarly conscious of his own deficiencies",
    "In this conflict of emotions all I dare aver is that it has been my faithful study to collect my duty from a just appreciation of every circumstance by which it might be affected",
    "All I dare hope is that if, in executing this task, I have been too much swayed by a grateful remembrance of former instances, or by an affectionate sensibility to this transcendent proof of the confidence of my fellow-citizens, and have thence too little consulted my incapacity as well as disinclination for the weighty and untried cares before me, my error will be palliated by the motives which mislead me, and its consequences be judged by my country with some share of the partiality in which they originated",
    "Such being the impressions under which I have, in obedience to the public summons, repaired to the present station, it would be peculiarly improper to omit in this first official act my fervent supplications to that Almighty Being who rules over the universe, who presides in the councils of nations, and whose providential aids can supply every human defect, that His benediction may consecrate to the liberties and happiness of the people of the United States a Government instituted by themselves for these essential purposes, and may enable every instrument employed in its administration to execute with success the functions allotted to his charge",
    "In tendering this homage to the Great Author of every public and private good, I assure myself that it expresses your sentiments not less than my own, nor those of my fellow-citizens at large less than either",
    "No people can be bound to acknowledge and adore the Invisible Hand which conducts the affairs of men more than those of the United States",
    "Every step by which they have advanced to the character of an independent nation seems to have been distinguished by some token of providential agency; and in the important revolution just accomplished in the system of their united government the tranquil deliberations and voluntary consent of so many distinct communities from which the event has resulted can not be compared with the means by which most governments have been established without some return of pious gratitude, along with an humble anticipation of the future blessings which the past seem to presage",
    "These reflections, arising out of the present crisis, have forced themselves too strongly on my mind to be suppressed",
    "You will join with me, I trust, in thinking that there are none under the influence of which the proceedings of a new and free government can more auspiciously commence",
    "By the article establishing the executive department it is made the duty of the President to recommend to your consideration such measures as he shall judge necessary and expedient",
    "The circumstances under which I now meet you will acquit me from entering into that subject further than to refer to the great constitutional charter under which you are assembled, and which, in defining your powers, designates the objects to which your attention is to be given",
    "It will be more consistent with those circumstances, and far more congenial with the feelings which actuate me, to substitute, in place of a recommendation of particular measures, the tribute that is due to the talents, the rectitude, and the patriotism which adorn the characters selected to devise and adopt them",
    "In these honorable qualifications I behold the surest pledges that as on one side no local prejudices or attachments, no separate views nor party animosities, will misdirect the comprehensive and equal eye which ought to watch over this great assemblage of communities and interests, so, on another, that the foundation of our national policy will be laid in the pure and immutable principles of private morality, and the preeminence of free government be exemplified by all the attributes which can win the affections of its citizens and command the respect of the world",
    "I dwell on this prospect with every satisfaction which an ardent love for my country can inspire, since there is no truth more thoroughly established than that there exists in the economy and course of nature an indissoluble union between virtue and happiness; between duty and advantage; between the genuine maxims of an honest and magnanimous policy and the solid rewards of public prosperity and felicity; since we ought to be no less persuaded that the propitious smiles of Heaven can never be expected on a nation that disregards the eternal rules of order and right which Heaven itself has ordained; and since the preservation of the sacred fire of liberty and the destiny of the republican model of government are justly considered, perhaps, as deeply, as finally, staked on the experiment entrusted to the hands of the American people"
    "Besides the ordinary objects submitted to your care, it will remain with your judgment to decide how far an exercise of the occasional power delegated by the fifth article of the Constitution is rendered expedient at the present juncture by the nature of objections which have been urged against the system, or by the degree of inquietude which has given birth to them"
    "Instead of undertaking particular recommendations on this subject, in which I could be guided by no lights derived from official opportunities, I shall again give way to my entire confidence in your discernment and pursuit of the public good; for I assure myself that whilst you carefully avoid every alteration which might endanger the benefits of an united and effective government, or which ought to await the future lessons of experience, a reverence for the characteristic rights of freemen and a regard for the public harmony will sufficiently influence your deliberations on the question how far the former can be impregnably fortified or the latter be safely and advantageously promoted"        
    "To the foregoing observations I have one to add, which will be most properly addressed to the House of Representatives"
    "It concerns myself, and will therefore be as brief as possible"
    "When I was first honored with a call into the service of my country, then on the eve of an arduous struggle for its liberties, the light in which I contemplated my duty required that I should renounce every pecuniary compensation"
    "From this resolution I have in no instance departed; and being still under the impressions which produced it, I must decline as inapplicable to myself any share in the personal emoluments which may be indispensably included in a permanent provision for the executive department, and must accordingly pray that the pecuniary estimates for the station in which I am placed may during my continuance in it be limited to such actual expenditures as the public good may be thought to require"
    "Having thus imparted to you my sentiments as they have been awakened by the occasion which brings us together, I shall take my present leave; but not without resorting once more to the benign Parent of the Human Race in humble supplication that, since He has been pleased to favor the American people with opportunities for deliberating in perfect tranquillity, and dispositions for deciding with unparalleled unanimity on a form of government for the security of their union and the advancement of their happiness, so His divine blessing may be equally conspicuous in the enlarged views, the temperate consultations, and the wise measures on which the success of this Government must depend"

    ]
    
    speech2=list()
    speech2=["Fellow Citizens"
    "I AM again called upon by the voice of my country to execute the functions of its Chief Magistrate",
    "When the occasion proper for it shall arrive, I shall endeavor to express the high sense I entertain of this distinguished honor, and of the confidence which has been reposed in me by the people of united America",
    "Previous to the execution of any official act of the President the Constitution requires an oath of office",
    "This oath I am now about to take, and in your presence: That if it shall be found during my administration of the Government I have in any instance violated willingly or knowingly the injunctions thereof, I may (besides incurring constitutional punishment) be subject to the upbraidings of all who are now witnesses of the present solemn ceremony"
    ]
    
    Speech1()
    Speech2()
    
    
    
def main():
    lab10()

if __name__=="__main__":
    main()