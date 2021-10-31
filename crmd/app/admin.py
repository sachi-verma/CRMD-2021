from django.contrib import admin
from .models import Debate, Score, CalculatedScore, FinalScore, AdjScore, AdjudicatorCalculatedScores

admin.site.site_header = 'CRMD 2021'
admin.site.site_title = 'CRMD 2021'
admin.site.index_title = 'CRMD 2021'

class ScoreAdmin(admin.ModelAdmin):
    fieldsets=(
    ('Debate Details', {
        'fields': ('dnum', 'prop', 'opp')
    }),
        
    ('Proposition Speaker 1 (JUDGE 1)', {
        'fields': (('props1p1j1','props1p2j1', 'props1p3j1'), ('props1p4j1', 'props1p5j1', 'props1p6j1'))
    }),

    ('Proposition Speaker 2 (JUDGE 1)', {
        'fields': (('props2p1j1','props2p2j1', 'props2p3j1'), ('props2p4j1', 'props2p5j1', 'props2p6j1'))
    }),

    ('Opposition Speaker 1 (JUDGE 1)', {
        'fields': (('opps1p1j1','opps1p2j1', 'opps1p3j1'), ('opps1p4j1', 'opps1p5j1', 'opps1p6j1'))
    }),

    ('Opposition Speaker 2 (JUDGE 1)', {
        'fields': (('opps2p1j1','opps2p2j1', 'opps2p3j1'), ('opps2p4j1', 'opps2p5j1', 'opps2p6j1'))
    }),

    ('Proposition Speaker 1 (JUDGE 2)', {
        'fields': (('props1p1j2','props1p2j2', 'props1p3j2'), ('props1p4j2', 'props1p5j2', 'props1p6j2'))
    }),

    ('Proposition Speaker 2 (JUDGE 2)', {
        'fields': (('props2p1j2','props2p2j2', 'props2p3j2'), ('props2p4j2', 'props2p5j2', 'props2p6j2'))
    }),

    ('Opposition Speaker 1 (JUDGE 2)', {
        'fields': (('opps1p1j2','opps1p2j2', 'opps1p3j2'), ('opps1p4j2', 'opps1p5j2', 'opps1p6j2'))
    }),

    ('Opposition Speaker 2 (JUDGE 2)', {
        'fields': (('opps2p1j2','opps2p2j2', 'opps2p3j2'), ('opps2p4j2', 'opps2p5j2', 'opps2p6j2'))
    }),
    )

class FinalScoreAdmin(admin.ModelAdmin):
    fieldsets=(
    ('Debate Details', {
        'fields': ('dnum', 'prop', 'opp')
    }),
        
    ('Proposition Speaker 1 (JUDGE 1)', {
        'fields': (('props1p1j1','props1p2j1', 'props1p3j1'), ('props1p4j1', 'props1p5j1', 'props1p6j1'))
    }),

    ('Proposition Speaker 2 (JUDGE 1)', {
        'fields': (('props2p1j1','props2p2j1', 'props2p3j1'), ('props2p4j1', 'props2p5j1', 'props2p6j1'))
    }),

    ('Opposition Speaker 1 (JUDGE 1)', {
        'fields': (('opps1p1j1','opps1p2j1', 'opps1p3j1'), ('opps1p4j1', 'opps1p5j1', 'opps1p6j1'))
    }),

    ('Opposition Speaker 2 (JUDGE 1)', {
        'fields': (('opps2p1j1','opps2p2j1', 'opps2p3j1'), ('opps2p4j1', 'opps2p5j1', 'opps2p6j1'))
    }),

    ('Proposition Speaker 1 (JUDGE 2)', {
        'fields': (('props1p1j2','props1p2j2', 'props1p3j2'), ('props1p4j2', 'props1p5j2', 'props1p6j2'))
    }),

    ('Proposition Speaker 2 (JUDGE 2)', {
        'fields': (('props2p1j2','props2p2j2', 'props2p3j2'), ('props2p4j2', 'props2p5j2', 'props2p6j2'))
    }),

    ('Opposition Speaker 1 (JUDGE 2)', {
        'fields': (('opps1p1j2','opps1p2j2', 'opps1p3j2'), ('opps1p4j2', 'opps1p5j2', 'opps1p6j2'))
    }),

    ('Opposition Speaker 2 (JUDGE 2)', {
        'fields': (('opps2p1j2','opps2p2j2', 'opps2p3j2'), ('opps2p4j2', 'opps2p5j2', 'opps2p6j2'))
    }),

    ('Proposition Speaker 1 (JUDGE 3)', {
        'fields': (('props1p1j3','props1p2j3', 'props1p3j3'), ('props1p4j3', 'props1p5j3', 'props1p6j3'))
    }),

    ('Proposition Speaker 2 (JUDGE 3)', {
        'fields': (('props2p1j3','props2p2j3', 'props2p3j3'), ('props2p4j3', 'props2p5j3', 'props2p6j3'))
    }),

    ('Opposition Speaker 1 (JUDGE 3)', {
        'fields': (('opps1p1j3','opps1p2j3', 'opps1p3j3'), ('opps1p4j3', 'opps1p5j3', 'opps1p6j3'))
    }),

    ('Opposition Speaker 2 (JUDGE 3)', {
        'fields': (('opps2p1j3','opps2p2j3', 'opps2p3j3'), ('opps2p4j3', 'opps2p5j3', 'opps2p6j3'))
    })
    )

class AdjScoreAdmin(admin.ModelAdmin):
    list_display = ("dnum", "adjudicator")

class AdjudicatorCalculatedScoresAdmin(admin.ModelAdmin):
    list_display = ("dnum", "adjudicator", "adjscore")



# Register your models here.
admin.site.register(Debate)
admin.site.register(Score, ScoreAdmin)
admin.site.register(CalculatedScore)
admin.site.register(FinalScore, FinalScoreAdmin)
admin.site.register(AdjScore, AdjScoreAdmin)
admin.site.register(AdjudicatorCalculatedScores, AdjudicatorCalculatedScoresAdmin)




