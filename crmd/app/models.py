from django.db import models
from django.db.models.signals import post_save

SIDE = (
    ('Proposition', 'Proposition'),
    ('Opposition', 'Opposition')
)

MOTION = (
    ('This house proposes more institutions like the Black Mountain College', 'This house proposes more institutions like the Black Mountain College'),
    ('This house will heavily penalise corporations for punishing their employees for engaging in legally permitted speech', 'This house will heavily penalise corporations for punishing their employees for engaging in legally permitted speech'),
    ('This house believes that all wealth beyond the necessary to meet ones basic needs is immoral', 'This house believes that all wealth beyond the necessary to meet ones basic needs is immoral'),
    ('This house believes that religious organizations should be subject to all aspects of civilian law (including, but not limited to: employment practice, adoption policy,...)', 'This house believes that religious organizations should be subject to all aspects of civilian law (including, but not limited to: employment practice, adoption policy,...)'),
    ('This house will pay known gang members to not commit violent crime', 'This house will pay known gang members to not commit violent crime'),
    ('This house believes that in times of crisis that threaten the existence of a community (eg: famine, war, plague natural disaster, etc), capable individuals from the community have a moral obligation to dedicate their time directly towards ending the crisis instead of pursuing nonessential activities (eg: playing sports, making non-propagandist/apolitical art, going on vacation to the beach, pursuing education irrrelevant to the crisis, etc)', 'This house believes that in times of crisis that threaten the existence of a community (eg: famine, war, plague natural disaster, etc), capable individuals from the community have a moral obligation to dedicate their time directly towards ending the crisis instead of pursuing nonessential activities (eg: playing sports, making non-propagandist/apolitical art, going on vacation to the beach, pursuing education irrrelevant to the crisis, etc)'),
    ('This house proposes the rule of the governing AI, with elections on priorities over, traditional representative democracy. For the purposes of this debate, there exists a governing AI. The governing AI is able to optimise policy outcomes to maximise or minimize measurable parameters it is given.',
    'This house proposes the rule of the governing AI, with elections on priorities over, traditional representative democracy. For the purposes of this debate, there exists a governing AI. The governing AI is able to optimise policy outcomes to maximise or minimize measurable parameters it is given.')
)
# Create your models here.
class Debate(models.Model):
    dnum = models.PositiveIntegerField()
    team = models.CharField(max_length=5)
    side = models.CharField(max_length=15, choices=SIDE)
    motion = models.CharField(max_length=1000)
    context = models.CharField(max_length=5000)
    link = models.URLField(max_length=100)
    meetingid = models.CharField(max_length=20)
    passcode = models.CharField(max_length=10)

    def __str__(self):
        return "Debate " + str(self.dnum) + " - " + self.team + " - " + self.side

class Score(models.Model):
    dnum = models.PositiveIntegerField()
    prop = models.CharField(max_length=5)
    opp = models.CharField(max_length=5)
    props1p1j1 = models.FloatField(verbose_name='Proposition Speaker 1 - Diction and Confidence - J1')
    props1p2j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Organization  and Clarity of Points - J1')
    props1p3j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Engagement with the Opposition - J1')
    props1p4j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Co-ordination with partner - J1')
    props1p5j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Use of Rebuttal - J1')
    props1p6j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Analysis - J1')
    props2p1j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Diction and Confidence - J1')
    props2p2j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Organization  and Clarity of Points - J1')
    props2p3j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Engagement with the Opposition - J1')
    props2p4j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Co-ordination with partner - J1')
    props2p5j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Use of Rebutta - J1')
    props2p6j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Analysis - J1')
    opps1p1j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Diction and Confidence - J1')
    opps1p2j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Organization  and Clarity of Points - J1')
    opps1p3j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Engagement with the Opposition - J1')
    opps1p4j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Co-ordination with partner - J1')
    opps1p5j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Use of Rebuttal - J1')
    opps1p6j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Analysis - J1')
    opps2p1j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Diction and Confidence - J1')
    opps2p2j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Organization  and Clarity of Points - J1')
    opps2p3j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Engagement with the Opposition - J1')
    opps2p4j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Co-ordination with partner - J1')
    opps2p5j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Use of Rebuttal - J1')
    opps2p6j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Analysis - J1')
    props1p1j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Diction and Confidence - J2')
    props1p2j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Organization  and Clarity of Points - J2')
    props1p3j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Engagement with the Opposition - J2')
    props1p4j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Co-ordination with partner - J2')
    props1p5j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Use of Rebuttal - J2')
    props1p6j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Analysis - J2')
    props2p1j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Diction and Confidence - J2')
    props2p2j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Organization  and Clarity of Points - J2')
    props2p3j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Engagement with the Opposition - J2')
    props2p4j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Co-ordination with partner - J2')
    props2p5j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Use of Rebuttal - J2')
    props2p6j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Analysis - J2')
    opps1p1j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Diction and Confidence - J2')
    opps1p2j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Organization  and Clarity of Points - J2')
    opps1p3j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Engagement with the Opposition - J2')
    opps1p4j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Co-ordination with partner - J2')
    opps1p5j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Use of Rebuttal - J2')
    opps1p6j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Analysis - J2')
    opps2p1j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Diction and Confidence - J2')
    opps2p2j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Organization  and Clarity of Points - J2')
    opps2p3j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Engagement with the Opposition - J2')
    opps2p4j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Co-ordination with partner - J2')
    opps2p5j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Use of Rebuttal - J2')
    opps2p6j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Analysis - J2')

    def __str__(self):
        return "Scores of Debate - " + str(self.dnum)

class CalculatedScore(models.Model):
    dnum = models.PositiveIntegerField()
    prop = models.CharField(max_length=5)
    opp = models.CharField(max_length=5)
    pscore = models.FloatField()
    oscore = models.FloatField()

    def __str__(self):
        return "Final score of Debate - " + str(self.dnum)

def get_or_create_calculated_scores(sender, instance, created, **kwargs):
    if created:
        a = (float(instance.props1p1j1) * 0.1 +
        float(instance.props1p2j1) * 0.1 +
        float(instance.props1p3j1) * 0.3 +
        float(instance.props1p4j1) * 0.2 +
        float(instance.props1p5j1) * 0.2 +
        float(instance.props1p6j1) * 0.1)
        b = (float(instance.props1p1j2) * 0.1 +
        float(instance.props1p2j2) * 0.1 +
        float(instance.props1p3j2) * 0.3 +
        float(instance.props1p4j2) * 0.2 +
        float(instance.props1p5j2) * 0.2 +
        float(instance.props1p6j2) * 0.1)
        props1 = (a + b) / 2
        
        c = (float(instance.props2p1j1) * 0.1 +
        float(instance.props2p2j1) * 0.1 +
        float(instance.props2p3j1) * 0.3 +
        float(instance.props2p4j1) * 0.2 +
        float(instance.props2p5j1) * 0.2 +
        float(instance.props2p6j1) * 0.1)
        d = (float(instance.props2p1j2) * 0.1 +
        float(instance.props2p2j2) * 0.1 +
        float(instance.props2p3j2) * 0.3 +
        float(instance.props2p4j2) * 0.2 +
        float(instance.props2p5j2) * 0.2 +
        float(instance.props2p6j2) * 0.1)
        props2 = (c + d) / 2

        prop = (props1 + props2) / 2
        prop = "{:.3f}".format(prop)

        x = (float(instance.opps1p1j1) * 0.1 +
        float(instance.opps1p2j1) * 0.1 +
        float(instance.opps1p3j1) * 0.3 +
        float(instance.opps1p4j1) * 0.2 +
        float(instance.opps1p5j1) * 0.2 +
        float(instance.opps1p6j1) * 0.1)
        y = (float(instance.opps1p1j2) * 0.1 +
        float(instance.opps1p2j2) * 0.1 +
        float(instance.opps1p3j2) * 0.3 +
        float(instance.opps1p4j2) * 0.2 +
        float(instance.opps1p5j2) * 0.2 +
        float(instance.opps1p6j2) * 0.1)
        opps1 = (x + y) / 2

        z = (float(instance.opps2p1j1) * 0.1 +
        float(instance.opps2p2j1) * 0.1 +
        float(instance.opps2p3j1) * 0.3 +
        float(instance.opps2p4j1) * 0.2 +
        float(instance.opps2p5j1) * 0.2 +
        float(instance.opps2p6j1) * 0.1)
        w = (float(instance.opps2p1j2) * 0.1 +
        float(instance.opps2p2j2) * 0.1 +
        float(instance.opps2p3j2) * 0.3 +
        float(instance.opps2p4j2) * 0.2 +
        float(instance.opps2p5j2) * 0.2 +
        float(instance.opps2p6j2) * 0.1)
        opps2 = (z + w) / 2

        opp = (opps1 + opps2) / 2
        opp = "{:.3f}".format(opp)

        CalculatedScore.objects.get_or_create(dnum=instance.dnum, prop=instance.prop, opp=instance.opp, pscore=prop, oscore=opp)
        
post_save.connect(get_or_create_calculated_scores, sender=Score)

class FinalScore(models.Model):
    dnum = models.PositiveIntegerField()
    prop = models.CharField(max_length=5)
    opp = models.CharField(max_length=5)
    props1p1j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Diction and Confidence - J1')
    props1p2j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Organization  and Clarity of Points - J1')
    props1p3j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Engagement with the Opposition - J1')
    props1p4j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Co-ordination with partner - J1')
    props1p5j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Use of Rebuttal - J1')
    props1p6j1 = models.FloatField( verbose_name='Proposition Speaker 1 - Analysis - J1')
    props2p1j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Diction and Confidence - J1')
    props2p2j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Organization  and Clarity of Points - J1')
    props2p3j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Engagement with the Opposition - J1')
    props2p4j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Co-ordination with partner - J1')
    props2p5j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Use of Rebuttal - J1')
    props2p6j1 = models.FloatField( verbose_name='Proposition Speaker 2 - Analysis - J1')
    opps1p1j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Diction and Confidence - J1')
    opps1p2j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Organization  and Clarity of Points - J1')
    opps1p3j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Engagement with the Opposition - J1')
    opps1p4j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Co-ordination with partner - J1')
    opps1p5j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Use of Rebuttal - J1')
    opps1p6j1 = models.FloatField( verbose_name='Opposition Speaker 1 - Analysis - J1')
    opps2p1j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Diction and Confidence - J1')
    opps2p2j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Organization  and Clarity of Points - J1')
    opps2p3j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Engagement with the Opposition - J1')
    opps2p4j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Co-ordination with partner - J1')
    opps2p5j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Use of Rebuttal - J1')
    opps2p6j1 = models.FloatField( verbose_name='Opposition Speaker 2 - Analysis - J1')
    props1p1j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Diction and Confidence - J2')
    props1p2j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Organization  and Clarity of Points - J2')
    props1p3j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Engagement with the Opposition - J2')
    props1p4j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Co-ordination with partner - J2')
    props1p5j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Use of Rebuttal - J2')
    props1p6j2 = models.FloatField( verbose_name='Proposition Speaker 1 - Analysis - J2')
    props2p1j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Diction and Confidence - J2')
    props2p2j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Organization  and Clarity of Points - J2')
    props2p3j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Engagement with the Opposition - J2')
    props2p4j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Co-ordination with partner - J2')
    props2p5j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Use of Rebuttal - J2')
    props2p6j2 = models.FloatField( verbose_name='Proposition Speaker 2 - Analysis - J2')
    opps1p1j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Diction and Confidence - J2')
    opps1p2j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Organization  and Clarity of Points - J2')
    opps1p3j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Engagement with the Opposition - J2')
    opps1p4j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Co-ordination with partner - J2')
    opps1p5j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Use of Rebuttal - J2')
    opps1p6j2 = models.FloatField( verbose_name='Opposition Speaker 1 - Analysis - J2')
    opps2p1j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Diction and Confidence - J2')
    opps2p2j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Organization  and Clarity of Points - J2')
    opps2p3j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Engagement with the Opposition - J2')
    opps2p4j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Co-ordination with partner - J2')
    opps2p5j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Use of Rebuttal - J2')
    opps2p6j2 = models.FloatField( verbose_name='Opposition Speaker 2 - Analysis - J2')
    props1p1j3 = models.FloatField( verbose_name='Proposition Speaker 1 - Diction and Confidence - j3')
    props1p2j3 = models.FloatField( verbose_name='Proposition Speaker 1 - Organization  and Clarity of Points - j3')
    props1p3j3 = models.FloatField( verbose_name='Proposition Speaker 1 - Engagement with the Opposition - j3')
    props1p4j3 = models.FloatField( verbose_name='Proposition Speaker 1 - Co-ordination with partner - j3')
    props1p5j3 = models.FloatField( verbose_name='Proposition Speaker 1 - Use of Rebuttal - j3')
    props1p6j3 = models.FloatField( verbose_name='Proposition Speaker 1 - Analysis - j3')
    props2p1j3 = models.FloatField( verbose_name='Proposition Speaker 2 - Diction and Confidence - j3')
    props2p2j3 = models.FloatField( verbose_name='Proposition Speaker 2 - Organization  and Clarity of Points - j3')
    props2p3j3 = models.FloatField( verbose_name='Proposition Speaker 2 - Engagement with the Opposition - j3')
    props2p4j3 = models.FloatField( verbose_name='Proposition Speaker 2 - Co-ordination with partner - j3')
    props2p5j3 = models.FloatField( verbose_name='Proposition Speaker 2 - Use of Rebuttal - j3')
    props2p6j3 = models.FloatField( verbose_name='Proposition Speaker 2 - Analysis - j3')
    opps1p1j3 = models.FloatField( verbose_name='Opposition Speaker 1 - Diction and Confidence - j3')
    opps1p2j3 = models.FloatField( verbose_name='Opposition Speaker 1 - Organization  and Clarity of Points - j3')
    opps1p3j3 = models.FloatField( verbose_name='Opposition Speaker 1 - Engagement with the Opposition - j3')
    opps1p4j3 = models.FloatField( verbose_name='Opposition Speaker 1 - Co-ordination with partner - j3')
    opps1p5j3 = models.FloatField( verbose_name='Opposition Speaker 1 - Use of Rebuttal - j3')
    opps1p6j3 = models.FloatField( verbose_name='Opposition Speaker 1 - Analysis - j3')
    opps2p1j3 = models.FloatField( verbose_name='Opposition Speaker 2 - Diction and Confidence - j3')
    opps2p2j3 = models.FloatField( verbose_name='Opposition Speaker 2 - Organization  and Clarity of Points - j3')
    opps2p3j3 = models.FloatField( verbose_name='Opposition Speaker 2 - Engagement with the Opposition - j3')
    opps2p4j3 = models.FloatField( verbose_name='Opposition Speaker 2 - Co-ordination with partner - j3')
    opps2p5j3 = models.FloatField( verbose_name='Opposition Speaker 2 - Use of Rebuttal - j3')
    opps2p6j3 = models.FloatField( verbose_name='Opposition Speaker 2 - Analysis - j3')

    def __str__(self):
        return "Scores of Debate - " + str(self.dnum)

def get_or_create_final_calculated_scores(sender, instance, created, **kwargs):
    if created:
        a = (float(instance.props1p1j1) * 0.1 +
        float(instance.props1p2j1) * 0.3 +
        float(instance.props1p3j1) * 0.2 +
        float(instance.props1p4j1) * 0.1 +
        float(instance.props1p5j1) * 0.2 +
        float(instance.props1p6j1) * 0.1)
        b = (float(instance.props1p1j2) * 0.1 +
        float(instance.props1p2j2) * 0.3 +
        float(instance.props1p3j2) * 0.2 +
        float(instance.props1p4j2) * 0.1 +
        float(instance.props1p5j2) * 0.2 +
        float(instance.props1p6j2) * 0.1)
        c = (float(instance.props2p1j3) * 0.1 +
        float(instance.props2p2j3) * 0.3 +
        float(instance.props2p3j3) * 0.2 +
        float(instance.props2p4j3) * 0.1 +
        float(instance.props2p5j3) * 0.2 +
        float(instance.props2p6j3) * 0.1)
        props1 = (a + b + c) / 3
        
        d = (float(instance.props2p1j1) * 0.1 +
        float(instance.props2p2j1) * 0.3 +
        float(instance.props2p3j1) * 0.2 +
        float(instance.props2p4j1) * 0.1 +
        float(instance.props2p5j1) * 0.2 +
        float(instance.props2p6j1) * 0.1)
        e = (float(instance.props2p1j2) * 0.1 +
        float(instance.props2p2j2) * 0.3 +
        float(instance.props2p3j2) * 0.2 +
        float(instance.props2p4j2) * 0.1 +
        float(instance.props2p5j2) * 0.2 +
        float(instance.props2p6j2) * 0.1)
        f = (float(instance.props2p1j3) * 0.1 +
        float(instance.props2p2j3) * 0.3 +
        float(instance.props2p3j3) * 0.2 +
        float(instance.props2p4j3) * 0.1 +
        float(instance.props2p5j3) * 0.2 +
        float(instance.props2p6j3) * 0.1)
        props2 = (d + e + f) / 3

        prop = (props1 + props2) / 2
        prop = "{:.3f}".format(prop)

        x = (float(instance.opps1p1j1) * 0.1 +
        float(instance.opps1p2j1) * 0.3 +
        float(instance.opps1p3j1) * 0.2 +
        float(instance.opps1p4j1) * 0.1 +
        float(instance.opps1p5j1) * 0.2 +
        float(instance.opps1p6j1) * 0.1)
        y = (float(instance.opps1p1j2) * 0.1 +
        float(instance.opps1p2j2) * 0.3 +
        float(instance.opps1p3j2) * 0.2 +
        float(instance.opps1p4j2) * 0.1 +
        float(instance.opps1p5j2) * 0.2 +
        float(instance.opps1p6j2) * 0.1)
        z = (float(instance.props2p1j3) * 0.1 +
        float(instance.props2p2j3) * 0.3 +
        float(instance.props2p3j3) * 0.2 +
        float(instance.props2p4j3) * 0.1 +
        float(instance.props2p5j3) * 0.2 +
        float(instance.props2p6j3) * 0.1)
        opps1 = (x + y + z) / 3

        u = (float(instance.opps2p1j1) * 0.1 +
        float(instance.opps2p2j1) * 0.3 +
        float(instance.opps2p3j1) * 0.2 +
        float(instance.opps2p4j1) * 0.1 +
        float(instance.opps2p5j1) * 0.2 +
        float(instance.opps2p6j1) * 0.1)
        v = (float(instance.opps2p1j2) * 0.1 +
        float(instance.opps2p2j2) * 0.3 +
        float(instance.opps2p3j2) * 0.2 +
        float(instance.opps2p4j2) * 0.1 +
        float(instance.opps2p5j2) * 0.2 +
        float(instance.opps2p6j2) * 0.1)
        w = (float(instance.props2p1j3) * 0.1 +
        float(instance.props2p2j3) * 0.3 +
        float(instance.props2p3j3) * 0.2 +
        float(instance.props2p4j3) * 0.1 +
        float(instance.props2p5j3) * 0.2 +
        float(instance.props2p6j3) * 0.1)
        opps2 = (u + v + w) / 3

        opp = (opps1 + opps2) / 2
        opp = "{:.3f}".format(opp)

        CalculatedScore.objects.get_or_create(dnum=instance.dnum, prop=instance.prop, opp=instance.opp, pscore=prop, oscore=opp)
        
post_save.connect(get_or_create_final_calculated_scores, sender=FinalScore)

class AdjScore(models.Model):
    dnum = models.PositiveIntegerField()
    prop = models.CharField(max_length=5)
    opp = models.CharField(max_length=5)
    adjudicator = models.CharField(max_length=20)
    propc1 = models.FloatField( verbose_name='Convincing ability - Prop')
    propc2 = models.FloatField( verbose_name='Reasoning - Prop')
    propc3 = models.FloatField( verbose_name='Analysis - Prop')
    oppc1 = models.FloatField( verbose_name='Convincing ability - Opp')
    oppc2 = models.FloatField( verbose_name='Reasoning - Opp')
    oppc3 = models.FloatField( verbose_name='Analysis - Opp')

    def __str__(self):
        return str(self.dnum)

class AdjudicatorCalculatedScores(models.Model):
    dnum = models.PositiveIntegerField()
    prop = models.CharField(max_length=5)
    opp = models.CharField(max_length=5)
    adjudicator = models.CharField(max_length=20)
    adjscore = models.FloatField()

    def __str__(self):
        return str(self.dnum)

def get_or_create_adj_calculated_scores(sender, instance, created, **kwargs):
    if created:
        p = (float(instance.propc1) + 
        float(instance.propc2) + 
        float(instance.propc3))
        prop_a = p / 3

        o = (float(instance.oppc1) + 
        float(instance.oppc2) + 
        float(instance.oppc3))
        opp_a = o / 3

        adj = (prop_a + opp_a) / 2
        adj = "{:.3f}".format(adj)

        AdjudicatorCalculatedScores.objects.get_or_create(dnum=instance.dnum, prop=instance.prop, opp=instance.opp, adjudicator=instance.adjudicator, adjscore=adj)
        

post_save.connect(get_or_create_adj_calculated_scores, sender=AdjScore)
