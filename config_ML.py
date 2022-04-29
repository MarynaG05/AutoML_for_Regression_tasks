import os

this_dir = os.path.dirname(os.path.realpath(__file__))

DATA_DIR = os.path.join(this_dir, "data")

PORTUGAL_ELECTION = os.path.join(DATA_DIR, "ElectionDataPortugal.csv")

PARKINSONS_TELEMONITORING = os.path.join(DATA_DIR, "parkinsons_updrs.csv")

METRO_INTERSTATE = os.path.join(DATA_DIR, "Metro_Interstate_Traffic_Volume.csv")


RANDOM_SEED= 42