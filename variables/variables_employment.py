import pandas as pd, numpy as np
from urbansim.utils import misc
import dataset

###
import orca
import utils
import pandana as pdna


#####################
# JOBS VARIABLES
#####################

@orca.column('jobs', cache=True, cache_scope='iteration')
def zone_id(jobs, buildings):
    return misc.reindex(buildings.zone_id, jobs.building_id)


@orca.column('jobs', cache=True, cache_scope='iteration')
def parcel_id(jobs, buildings):
    return misc.reindex(buildings.parcel_id, jobs.building_id)


@orca.column('jobs', cache=True, cache_scope='iteration')
def x(jobs, buildings):
    return misc.reindex(buildings.x, jobs.building_id)


@orca.column('jobs', cache=True, cache_scope='iteration')
def y(jobs, buildings):
    return misc.reindex(buildings.y, jobs.building_id)


@orca.column('jobs', cache=True, cache_scope='iteration')
def large_area_id(jobs, buildings):
    return misc.reindex(buildings.large_area_id, jobs.building_id)


@orca.column('jobs', cache=True, cache_scope='iteration')
def lid(jobs):
    return jobs.large_area_id


@orca.column('jobs', cache=True, cache_scope='iteration')
def nodeid_walk(jobs, buildings):
    return misc.reindex(buildings.nodeid_walk, jobs.building_id)


@orca.column('jobs', cache=True, cache_scope='iteration')
def nodeid_drv(jobs, buildings):
    return misc.reindex(buildings.nodeid_drv, jobs.building_id)
