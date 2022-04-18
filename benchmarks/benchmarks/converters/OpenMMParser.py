import MDAnalysis as mda
try:
    from MDAnalysisTests.datafiles import PDB
except:
    pass

try:
    from openmm import app
except ImportError:
    try:
        from simtk.openmm import app
    except ImportError:
        pass

class OpenMMAppTopologyParserBench(object):
    """Benchmarks for MDAnalysis.converters.OpenMMParser
    """
    parser = mda.converters.OpenMMParser.OpenMMTopologyParser

    def setup(self):
        self.omm_top = app.PDBFile(PDB).topology

    def time_parser(self):
        md_top = self.parser(self.omm_top).parse()
