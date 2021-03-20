import csv
import math

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, "rt", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=separator, quotechar=quote)
        for row in csv_reader:
            table[row[keyfield]] = row
    return table


def build_country_code_converter(codeinfo):


    dat = read_csv_as_nested_dict(codeinfo['codefile'],codeinfo['plot_codes'],codeinfo['separator'],codeinfo['quote'])

    table = {}

    for dit in dat:
        table[dit] = dat[dit][codeinfo['data_codes']]
        #print(dat[dit]['Code2'])
    return table



def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):

    table = {}

    no_appear = set()

    # for key in plot_countries:
    #     table[key] = None

    for key,val in plot_countries.items():

        for key2,val2 in gdp_countries.items():

            if val == val2['Country Name']:
                table[key] = val2['Country Code']

    if len(plot_countries) == len(table):
        no_appear = set()
    else:
        for key in plot_countries:
            if not key in table:
                no_appear.add(key)
    return table, no_appear


# this function still has some bugs:

def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
        Inputs:
          gdpinfo        - A GDP information dictionary
          codeinfo       - A country code information dictionary
          plot_countries - Dictionary mapping plot library country codes to country names
          year           - String year for which to create GDP mapping

        Output:
          A tuple containing a dictionary and two sets.  The dictionary
          maps country codes from plot_countries to the log (base 10) of
          the GDP value for that country in the specified year.  The first
          set contains the country codes from plot_countries that were not
          found in the GDP data file.  The second set contains the country
          codes from plot_countries that were found in the GDP data file, but
          have no GDP data for the specified year.
        """

    gdpdat = read_csv_as_nested_dict(gdpinfo['gdpfile'],year,gdpinfo['separator'],
                                 gdpinfo['quote'])

    codedat = build_country_code_converter(codeinfo)

    #print('codedat is ',codedat)
    table = {}
    no_gdp = set()
    no_appear = set()
    v2 = {v: k for k, v in plot_countries.items()}

    for key, val in codedat.items():
        for key2, val2 in gdpdat.items():
            if val.lower() == gdpdat[key2]['Code'].lower():
                try:
                    table[v2[key]] = math.log(float(key2), 10)
                    del v2[key]
                except ValueError:
                    if key in v2:
                        no_gdp.add(v2[key])
                        del v2[key]
                    else:
                        pass
    no_appear = set(v2.values())
    return table, no_appear, no_gdp



