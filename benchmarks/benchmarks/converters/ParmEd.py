import MDAnalysis as mda
try:
    from MDAnalysisTests.datafiles import GRO, PDB
    from MDAnalysisTests.coordinates.reference import RefAdKSmall
except:
    pass

try:
    import parmed as pmd
except:
    pass


class ParmEdReaderBenchBase(object):
    def setup(self, filename):
        self.pm_file = pmd.load_file(filename)

    def time_parmed_reader(self, filename):
        u = mda.Universe(self.pm_file)


class ParmEdGROReaderBench(ParmEdReaderBenchBase):
    params = (GRO, )
    param_names = ['filename']


class ParmEdPDBReaderBench(ParmEdReaderBenchBase):
    params = (RefAdKSmall.filename, )
    param_names = ['filename']


class ParmEdPConvertorBench(object):
    params = (GRO, )
    param_names = ['filename']

    def setup(self, filename):
        self.pm_file = pmd.load_file(filename)
        self.u = mda.Universe(self.pm_file)
    def time_parmed_convertor(self, filename):
        self.u.select_atoms('resname SOL').convert_to('PARMED')
