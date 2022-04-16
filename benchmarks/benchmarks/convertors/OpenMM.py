import MDAnalysis as mda
try:
    from MDAnalysisTests.datafiles import PDB, CONECT
    from MDAnalysisTests.coordinates.reference import RefAdKSmall
    from MDAnalysisTests.coordinates.base import _SingleFrameReader

except:
    pass

try:
    import openmm as mm
    from openmm import app, unit
except ImportError:
    try:
        from simtk.openmm import app
        from simtk import unit
        from simtk import openmm as mm
    except ImportError:
        pass


class OpenMMSimulationReaderBench():
    """
    Simple benchmark for OpenMM simulation reader
    """
    def setup(self):
        pdb = app.PDBFile(RefAdKSmall.filename)
        forcefield = app.ForceField("amber99sbildn.xml")
        system = forcefield.createSystem(
            pdb.topology, nonbondedMethod=app.NoCutoff, constraints=app.HBonds
        )
        integrator = mm.LangevinIntegrator(
            300 * unit.kelvin, 1 / unit.picoseconds, 2.0 * unit.femtoseconds
        )
        self.sim = app.Simulation(pdb.topology, system, integrator)
        self.sim.context.setPositions(pdb.positions)

    def time_simulation_reader(self):
        self.universe = mda.Universe(self.sim)


class OpenMMModellerReaderBench():
    """
     Bnchmark for OpenMM modeller
    """
    def setup(self):
        pdb_obj = app.PDBFile(RefAdKSmall.filename)
        self.modeller = app.Modeller(pdb_obj.topology, pdb_obj.positions)

    def time_openmm_modeller(self):
        self.universe = mda.Universe(self.modeller)


class OpenMMPDBReaderBench(object):
    """Benchmarks for MDAnalysis.converters.OpenMMParser
    functions.
    """
    parser = mda.converters.OpenMMParser.OpenMMTopologyParser

    params = (CONECT, PDB)
    param_names = ['filename']


    def setup(self, filename):
        self.pdb = app.PDBFile(filename)

    def time_parser(self, filename):
        u = mda.Universe(self.pdb)
