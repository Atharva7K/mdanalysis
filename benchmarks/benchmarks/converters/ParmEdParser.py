import MDAnalysis as mda
try:
    from MDAnalysisTests.datafiles import PSF_NAMD_GBIS
except:
    pass

try:
    import parmed as pmd
except:
    pass


class ParmEdTopologyParserBench(object):
    parser = mda.converters.ParmEdParser.ParmEdParser

    params = (PSF_NAMD_GBIS, )
    param_names = ['filename']


    def setup(self, filename):
        self.parm_top = pmd.load_file(filename)

    def time_parser(self, filename):
        md_top = self.parser(self.parm_top).parse()
