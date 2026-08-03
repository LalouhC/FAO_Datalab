class DataProfiler:

  def __init__(self, df):
    self.df = df

  def count_missing_values(self):
    return self.df.isnull().sum()

  def check_duplicates(self):
    return self.df.duplicated().sum()


class ProfileurFAO(DataProfiler):

  def __init__(self, df, file_name):
    super().__init__(df)
    self.file_name = file_name