import MDAnalysis as mda
try:
    from MDAnalysisTests.datafiles import CONECT, PDB
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

    params = (PDB, )
    param_names = ['filename']


    def setup(self, filename):
        self.omm_top = app.PDBFile(filename).topology

    def time_parser(self, filename):
        md_top = self.parser(self.omm_top).parse()
