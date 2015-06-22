__author__ = 'heilniem'


# These static choice lists were moved here from dictionary/models

handednessChoices = (('0', 'No Value Set'),
                     ('1', 'N/A'),
                     ('2', '1'),
                     ('3', '2'),
                     ('4', '2a'),
                     ('5', '2s'),
                     ('6', 'X'))

handshapeChoices = (('0', 'No Value Set'),
                    ('1', 'N/A'),
                    ('2', 'J + beak2'),
                    ('3', '5'),
                    ('4', 'Money'),
                    ('5', 'V'),
                    ('6', 'B'),
                    ('7', 'Y'),
                    ('8', 'S'),
                    ('9', 'L'),
                    ('10', 'Baby-c'),
                    ('11', 'B-relaxed'),
                    ('12', 'C-spread'),
                    ('13', 'B-curved'),
                    ('14', 'N'),
                    ('15', '1'),
                    ('16', 'W'),
                    ('17', 'Beak2'),
                    ('18', 'Q'),
                    ('19', '5r'),
                    ('20', 'V-curved'),
                    ('21', '1-curved'),
                    ('22', 'Beak'),
                    ('23', 'Beak2-spread'),
                    ('24', 'A'),
                    ('25', 'I'),
                    ('26', 'B-bent'),
                    ('27', 'C'),
                    ('28', 'T'),
                    ('29', 'Baby-beak'),
                    ('30', '5m'),
                    ('31', 'Shower'),
                    ('32', 'O'),
                    ('33', 'Flexed arm'),
                    ('34', 'D'),
                    ('35', '4'),
                    ('36', 'M + v'),
                    ('37', '3'),
                    ('38', 'Baby-o'),
                    ('39', 'F'),
                    ('40', 'M'),
                    ('41', 'Flower'),
                    ('42', 'K'),
                    ('43', '5mx'),
                    ('44', 'B + s'),
                    ('45', 'Asl-t'),
                    ('46', 'O2'),
                    ('47', 'R'),
                    ('48', '9'),
                    ('49', '5rx'),
                    ('50', 'Beak, pinkie extended'),
                    ('51', 'S + w'),
                    ('52', 'L2'),
                    ('53', 'L-curved'),
                    ('54', 'W-curved'),
                    ('55', 'Q5'),
                    ('56', 'E'),
                    ('57', 'T + l'),
                    ('58', 'N + e'),
                    ('59', 'Horns'),
                    ('60', 'P'),
                    ('61', 'C-spread, index extended'),
                    ('62', 'Baby-c'),
                    ('63', 'Money-open'),
                    ('64', 'Beak, index extended'),
                    ('65', '5px'),
                    ('66', 'Y mrp-bent'),
                    ('67', 'Mrp-bent'),
                    ('68', 'Mrp-curved'),
                    ('69', 'O3'),
                    ('70', 'T + v'),
                    ('71', 'V + o'),
                    ('72', 'C, extended index'),
                    ('73', '5 + v'),
                    ('74', 'A-curved'),
                    ('75', 'C-spread-2'),
                    ('76', 'J + l'),
                    ('77', 'J + n'),
                    ('78', 'L + mrp bent'),
                    ('79', 'O + k'),
                    ('80', 'Middle finger'),
                    ('81', '1 + m'),
                    ('82', 'S + i'))

locationChoices = (('0', 'No Value Set'),
                   ('1', 'N/A'),
                   ('2', 'Neutral space > head'),
                   ('3', 'Neutral space'),
                   ('4', 'Shoulder'),
                   ('5', 'Weak hand'),
                   ('6', 'Weak hand > arm'),
                   ('7', 'Forehead'),
                   ('8', 'Chest'),
                   ('9', 'Neck'),
                   ('10', 'Head'),
                   ('11', 'Weak hand: back'),
                   ('12', 'Chin'),
                   ('13', 'Ring finger'),
                   ('14', 'Forehead, belly'),
                   ('15', 'Eye'),
                   ('16', 'Cheekbone'),
                   ('17', 'Face'),
                   ('18', 'Ear'),
                   ('19', 'Mouth'),
                   ('20', 'Low in neutral space'),
                   ('21', 'Arm'),
                   ('22', 'Nose'),
                   ('23', 'Cheek'),
                   ('24', 'Heup'),
                   ('25', 'Body'),
                   ('26', 'Belly'),
                   ('27', 'Tongue'),
                   ('28', 'Chin > neutral space'),
                   ('29', 'Locative'),
                   ('30', 'Head ipsi'),
                   ('31', 'Forehead > chin'),
                   ('32', 'Head > shoulder'),
                   ('33', 'Chin > weak hand'),
                   ('34', 'Forehead > chest'),
                   ('35', 'Borst contra'),
                   ('36', 'Weak hand: palm'),
                   ('37', 'Back of head'),
                   ('38', 'Above head'),
                   ('39', 'Next to trunk'),
                   ('40', 'Under chin'),
                   ('41', 'Head > weak hand'),
                   ('42', 'Borst ipsi'),
                   ('43', 'Temple'),
                   ('44', 'Upper leg'),
                   ('45', 'Leg'),
                   ('46', 'Mouth ipsi'),
                   ('47', 'High in neutral space'),
                   ('48', 'Mouth > chest'),
                   ('49', 'Chin ipsi'),
                   ('50', 'Wrist'),
                   ('51', 'Lip'),
                   ('52', 'Neck > chest'),
                   ('53', 'Cheek + chin'),
                   ('54', 'Upper arm'),
                   ('55', 'Shoulder contra'),
                   ('56', 'Forehead > weak hand'),
                   ('57', 'Neck ipsi'),
                   ('58', 'Mouth > weak hand'),
                   ('59', 'Weak hand: thumb side'),
                   ('60', 'Between thumb and index finger'),
                   ('61', 'Neutral space: high'),
                   ('62', 'Chin contra'),
                   ('63', 'Upper lip'),
                   ('64', 'Forehead contra'),
                   ('65', 'Side of upper body'),
                   ('66', 'Weak hand: tips'),
                   ('67', 'Mouth + chin'),
                   ('68', 'Side of head'),
                   ('69', 'Head > neutral space'),
                   ('70', 'Chin > chest'),
                   ('71', 'Face + head'),
                   ('72', 'Cheek contra'),
                   ('73', 'Belly ipsi'),
                   ('74', 'Chest contra'),
                   ('75', 'Neck contra'),
                   ('76', 'Back of the head'),
                   ('77', 'Elbow'),
                   ('78', 'Temple > chest'),
                   ('79', 'Thumb'),
                   ('80', 'Middle finger'),
                   ('81', 'Pinkie'),
                   ('82', 'Index finger'),
                   ('83', 'Back'),
                   ('84', 'Ear > cheek'),
                   ('85', 'Knee'),
                   ('86', 'Shoulder contra > shoulder ipsi'),
                   ('87', 'Mouth + cheek'))

# these are values for prim2ndloc fin2ndloc introduced for BSL, the names
# might change
BSLsecondLocationChoices = (
    ('notset', 'No Value Set'),
    ('0', 'N/A'),
    ('back', 'Back'),
    ('palm', 'Palm'),
    ('radial', 'Radial'),
    ('ulnar', 'Ulnar'),
    ('fingertip(s)', 'Fingertips'),
    ('root', 'Root')
)

palmOrientationChoices = (
    ('notset', 'No Value Set'),
    ('prone', 'Prone'),
    ('neutral', 'Neutral'),
    ('supine', 'Supine'),
    ('0', 'N/A'),
)

relOrientationChoices = (
    ('notset', 'No Value Set'),
    ('palm', 'Palm'),
    ('back', 'Back'),
    ('root', 'Root'),
    ('radial', 'Radial'),
    ('ulnar', 'Ulnar'),
    ('fingertip(s)', 'Fingertips'),
    ('0', 'N/A'),
)

relation_between_articulators_choices = (
    ("0", 'No Value Set'),
    ("1", 'N/A'),
    ("2", 'One hand behind the other'),
    ("3", 'One hand above the other'),
    ("4", 'Hands move around each other'),
    ("5", 'Strong hand passes through weak hand'),
    ("6", 'One hand after the other'),
    ("7", 'One hand on top of the other'),
    ("8", 'Around the weak hand'),
    ("9", 'Strong hand moves through weak hand'),
    ("10", 'Fingers interwoven'),
    ("11", 'Weak hand within strong hand'),
    ("12", 'Hands rotate around each other'),
    ("13", 'Fingertips touching'),
    ("14", 'Passing under the weak hand'),
    ("15", 'Passing above the wrist'),
    ("16", 'Passing over the weak hand'),
    ("17", 'Strong hand behind weak hand'),
    ("18", 'Strong hand around weak hand'),
    ("19", 'Hands interlocked between thumb and index'),
    ("20", 'Hands cross'),
    ("21", 'Hands overlap'),
    ("22", 'Hand appears behind weak hand'),
    ("23", 'Strong hand under weak hand'),
    ("24", 'One hand above or beside the other'),
    ("25", 'Hands start crossed'),
    ("26", 'Hands move in tandem'),
    ("27", 'Interlocked'),
    ("28", 'One hand a bit higher'),
    ("29", 'Strong hand hangs across weak hand'),
    ("30", 'Strong hand moves over tips of weak hand'),
    ("31", 'Fingers interlocked'),
    ("32", 'Weak hand around thumb'),
    ("33", 'Movement mirrored'),
    ("34", 'Hands rotate around each other, then contacting movement'),
    ("35", 'Thumbs rotate about each other'),
    ("36", 'Hands rotate in the same direction'),
    ("37", 'Crossed'),
    ("38", 'Below the weak hand'),
)

absolute_orientation_palm_choices = (
    ('0', 'No Value Set'),
    ('1', 'N/A'),
    ('2', 'Downwards'),
    ('3', 'Towards each other'),
    ('4', 'Backwards'),
    ('5', 'Upwards'),
    ('6', 'Inwards'),
    ('7', 'Forwards'),
    ('8', 'Backwards > forwards'),
    ('9', 'Inwards, forwards'),
    ('10', 'Forwards, sidewards'),
    ('11', 'Downwards, sidewards'),
    ('12', 'Variable'),
    ('13', 'Outwards'),
    ('14', 'Backs towards each other'),
    ('15', 'Inwards > backwards'),
    ('16', 'Sidewards'),
    ('17', 'Forwards, downwards'),
)

absolute_orientation_fingers_choices = (
    ('0', 'No Value Set'),
    ('1', 'N/A'),
    ('2', 'Inwards'),
    ('3', 'Downwards'),
    ('4', 'Upwards'),
    ('5', 'Upwards, forwards'),
    ('6', 'Forwards'),
    ('7', 'Backwards'),
    ('8', 'Towards location'),
    ('9', 'Inwards, upwards'),
    ('10', 'Back/palm'),
    ('11', 'Towards each other'),
    ('12', 'Neutral'),
    ('13', 'Forwards > inwards'),
    ('14', 'Towards weak hand'),
)

relative_orientation_movement_choices = (
    ('0', 'No Value Set'),
    ('1', 'N/A'),
    ('2', 'Pinkie'),
    ('3', 'Palm'),
    ('4', 'Tips'),
    ('5', 'Thumb'),
    ('6', 'Basis'),
    ('7', 'Back'),
    ('8', 'Thumb/pinkie'),
    ('9', 'Variable'),
    ('10', 'Basis + palm'),
    ('11', 'Basis + basis'),
    ('12', 'Pinkie + back'),
    ('13', 'Palm > basis'),
    ('14', 'Palm > back'),
    ('15', 'Back > palm'),
    ('16', 'Basis, pinkie'),
    ('17', 'Pinkie > palm'),
    ('18', 'Basis > pinkie'),
    ('19', 'Pinkie > palm > thumb'),
    ('20', 'Back > basis'),
    ('21', 'Thumb > pinkie'),
)

relative_orientation_location_choices = (
    ('0', 'No Value Set'),
    ('1', 'N/A'),
    ('2', 'Pinkie/thumb'),
)

handChChoices = (
    ("0", 'No Value Set'),
    ("1", 'N/A'),
    ("2", '+ closing'),
    ("3", 'Closing, opening'),
    ("4", 'Closing a little'),
    ("5", 'Opening'),
    ("6", 'Closing'),
    ("7", 'Bending'),
    ("8", 'Curving'),
    ("9", 'Wiggle'),
    ("10", 'Unspreading'),
    ("11", 'Extension'),
    ("12", '>5'),
    ("13", 'Partly closing'),
    ("14", 'Closing one by one'),
    ("15", '>s'),
    ("16", '>b'),
    ("17", '>a'),
    ("18", '>1'),
    ("19", 'Wiggle, closing'),
    ("20", 'Thumb rubs finger'),
    ("21", 'Spreading'),
    ("22", '>i'),
    ("23", '>l'),
    ("24", '>5m'),
    ("25", 'Thumb rubs fingers'),
    ("26", 'Thumb curving'),
    ("27", 'Thumbfold'),
    ("28", 'Finger rubs thumb'),
    ("29", '>o'),
    ("30", '>t'),
    ("31", 'Extension one by one'),
)

movShapeChoices = (
    ("0", 'No Value Set'),
    ("1", 'N/A'),
    ("2", 'Circle sagittal > straight'),
    ("3", 'Rotation > straight'),
    ("4", 'Arc'),
    ("5", 'Rotation'),
    ("6", 'Straight'),
    ("7", 'Flexion'),
    ("8", 'Circle sagittal'),
    ("9", 'Arc horizontal'),
    ("10", 'Arc up'),
    ("11", 'Question mark'),
    ("12", 'Zigzag'),
    ("13", 'Arc outside'),
    ("14", 'Circle horizontal'),
    ("15", 'Extension'),
    ("16", 'Abduction'),
    ("17", 'Straight > abduction'),
    ("18", 'Z-shape'),
    ("19", 'Straight + straight'),
    ("20", 'Arc > straight'),
    ("21", 'Parallel arc > straight'),
    ("22", 'Zigzag > straight'),
    ("23", 'Arc down'),
    ("24", 'Arc + rotation'),
    ("25", 'Arc + flexion'),
    ("26", 'Circle parallel'),
    ("27", 'Arc front'),
    ("28", 'Circle horizontal small'),
    ("29", 'Arc back'),
    ("30", 'Waving'),
    ("31", 'Straight, rotation'),
    ("32", 'Circle parallel + straight'),
    ("33", 'Down'),
    ("34", 'Thumb rotation'),
    ("35", 'Circle sagittal small'),
    ("36", 'Heart-shape'),
    ("37", 'Circle'),
    ("38", 'Cross'),
    ("39", 'Supination'),
    ("40", 'Pronation'),
    ("41", 'M-shape'),
    ("42", 'Circle sagittal big'),
    ("43", 'Circle parallel small'),
)

movDirChoices = (
    ("0", 'No Value Set'),
    ("1", 'N/A'),
    ("2", '+ forward'),
    ("3", '> downwards'),
    ("4", '> forwards'),
    ("5", 'Backwards'),
    ("6", 'Backwards > downwards'),
    ("7", 'Directional'),
    ("8", 'Downwards'),
    ("9", 'Downwards + inwards'),
    ("10", 'Downwards + outwards'),
    ("11", 'Downwards > inwards'),
    ("12", 'Downwards > outwards'),
    ("13", 'Downwards > outwards, downwards'),
    ("14", 'Downwards, inwards'),
    ("15", 'Forward'),
    ("16", 'Forwards'),
    ("17", 'Forwards > downwards'),
    ("18", 'Forwards > inwards'),
    ("19", 'Forwards > sidewards > forwards'),
    ("20", 'Forwards-backwards'),
    ("21", 'Forwards, downwards'),
    ("22", 'Forwards, inwards'),
    ("23", 'Forwards, outwards'),
    ("24", 'Forwards, upwards'),
    ("25", 'Hands approach vertically'),
    ("26", 'Inwards'),
    ("27", 'Inwards > forwards'),
    ("28", 'Inwards, downwards'),
    ("29", 'Inwards, forwards'),
    ("30", 'Inwards, upwards'),
    ("31", 'No movement'),
    ("32", 'Upwards'),
    ("33", 'Upwards > downwards'),
    ("34", 'Up and down'),
    ("35", 'Upwards, inwards'),
    ("36", 'Upwards, outwards'),
    ("37", 'Upwards, forwards'),
    ("38", 'Outwards'),
    ("39", 'Outwards > downwards'),
    ("40", 'Outwards > downwards > inwards'),
    ("41", 'Outwards > upwards'),
    ("42", 'Outwards, downwards > downwards'),
    ("43", 'Outwards, forwards'),
    ("44", 'Outwards, upwards'),
    ("45", 'Rotation'),
    ("46", 'To and fro'),
    ("47", 'To and fro, forwards-backwards'),
    ("48", 'Upwards/downwards'),
    ("49", 'Variable'),
)

movManChoices = (
    ("0", 'No Value Set'),
    ("1", 'N/A'),
    ("2", 'Short'),
    ("3", 'Strong'),
    ("4", 'Slow'),
    ("5", 'Large, powerful'),
    ("6", 'Long'),
    ("7", 'Relaxed'),
    ("8", 'Trill'),
    ("9", 'Small'),
    ("10", 'Tense'),
)

contTypeChoices = (
    ("0", 'No Value Set'),
    ("1", 'N/A'),
    ("2", 'Brush'),
    ("3", 'Initial > final'),
    ("4", 'Final'),
    ("5", 'Initial'),
    ("6", 'Continuous'),
    ("7", 'Contacting hands'),
    ("8", 'Continuous + final'),
    ("9", 'None + initial'),
    ("10", '> final'),
    ("11", 'None + final'),
)

namedEntChoices = (
    ("0", 'No Value Set'),
    ("1", 'N/A'),
    ("2", 'Person'),
    ("3", 'Public figure'),
    ("4", 'Place'),
    ("5", 'Region'),
    ("6", 'Brand'),
    ("7", 'Country'),
    ("8", 'Device'),
    ("9", 'Product'),
    ("10", 'Project'),
    ("11", 'Place nickname'),
    ("12", 'Event'),
    ("13", 'Newspaper'),
    ("14", 'Story character'),
    ("15", 'Continent'),
    ("16", 'Organisation'),
    ("17", 'Company'),
    ("18", 'Team'),
    ("19", 'Drink'),
    ("20", 'Magazine'),
)