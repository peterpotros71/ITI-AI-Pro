package hw8.hw8;

import org.apache.commons.csv.CSVFormat;

import smile.data.DataFrame;
import smile.io.Read;

public class Utilis {
	
	smile.data.DataFrame df = null;
	public smile.data.DataFrame read_csv() {
    	try {
    		CSVFormat format = CSVFormat.DEFAULT.withFirstRecordAsHeader ();
    		df = Read.csv("cities.csv", format);
    	    System.out.println(df);
    		}
    		catch(Exception ex){	
    		}
    	return df;
	}
	
	public int get_average_population(String country_name) {
		DataFrame df = read_csv();
		DataFrame country_df = DataFrame.of(df.stream().filter(x -> x.get("country_name").equals(country_name)));
		System.out.println (country_df);
		Double average_population = country_df.stream()
				.mapToInt(x -> x.isNullAt("population") ? 0 : x.getInt("population"))
				.average().orElse(0.0);
		return average_population.intValue();
	}

}
