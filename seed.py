from models import db, Pet
from app import app

db.drop_all()
db.create_all()

kiko = Pet(name='Kiko', 
           species='dog', 
           photo_url='https://lh3.googleusercontent.com/pw/AP1GczM9lbIOLBc2ZpbNFxGhPtoszYZVJMJyOXXrA1MxBewHZBObQNuzsLznhjeEeF7snnjFpvfKabZhDhVrxayOlHOp2vRiT1pAKBF42eEeQpFERbv-5W4Rd9dtzrMAhkCCadeYlzSEBCUtKVsSm75DfjjlwfwH6hNGZE6B7D625kwjL5HrpK47c4Bse28tJQVMCOUyZ6_rurpkoKVoBbg1kziXSVXev8loyGv3wXgaSkwtGE7Y9Z_4fFcUhtQm_tQ1U9D_GB5ImCvd1xeO9dWu5sFwHjLY_Zi7ayh3q3UUafxz2Nf7xUTk2VEZRCcbQJ8ovPMTi14wIkpMaSePVK4PNVedS-VDaIb3Mdl1J65mpxUpN7UBHKLJjxSCvQeJwwuyIpCniMEEYhk4iROBFfWVgOz-CXJsspO1tUD9KBeShfOEmU_TDG4EE0R6BTvb0Hu4xIqORozLTY0M6gajNTVkTJbWJaS15UbVXe0WYOoTkiZ6gBHRrc_MA2TocxU7mtdbgMa6MI_QcRh8tmmuYdDBb2I1JRmTOw_VAVFOKxrOEQufLDgk__zVW5MEiagc467pzWY04-HxGvED9ZOA_rMGksbHhmX8SbSJouG12sb2yTg_lQ7gjoyIqpXgiBvLqqd6w2CSdWEfzJpCHi5kCIMghSj51uQLopoaY8ba9k6CM6AYdfRVSsa6cTu57Fh8LABm82Ls09BDeJ-rm30_ZLbiymDW3GR9TRoiz-vqTPdKODep_3OiqeG4fhxCsF62ii7N2PWJtnmkt3m8pLgBEaUC7pH3mAYfbQLZxXBOZRudc6RkQqcK1lDixc9JN_8mxw6K57-jhiLmjSOkp44NOQ0zxsbfqnQFa1a9HBQXw_TW8TwVgnBmHeAIC_odJyU8cxS8rwoJsIdFJZQbxWjIgrw86HdXHXm3=w1508-h1733-s-no-gm?authuser=0', 
           age=12, 
           notes='A lovely, stinky boy')
holly = Pet(name='Holly',
            species='cat',
            age=1,
            notes='rambunctious girl who loves other cats')
dinky = Pet(name='Dinky',
            species='porcupine',
            age=1,
            notes='gotta go fast, but not too fast')

db.session.add_all([kiko, holly, dinky])
db.session.commit()