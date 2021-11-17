package hw8.hw8;

import org.apache.commons.csv.CSVFormat;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import smile.data.DataFrame;
import smile.data.measure.NominalScale;
import smile.data.vector.IntVector;
import smile.io.Read;

@SpringBootApplication
public class Hw8Application {

	public static void main(String[] args) {
		
		Utilis utili = new Utilis();
		smile.data.DataFrame df = utili.read_csv();
    	
    	smile.data.DataFrame new_df = df.select ("city_code", "country_name", "population");
	    System.out.println(new_df.summary());
	    
	    String[] values = new_df.stringVector ("country_name").distinct ().toArray (new String[]{});
		int[] pclassValues = new_df.stringVector ("country_name").factorize (new NominalScale (values)).toIntArray ();
		new_df = new_df.merge (IntVector.of ("country_code", pclassValues));
		new_df = new_df.drop ("country_name");
		System.out.println ("=======Encoding Non Numeric Data==============");
		System.out.println (new_df.structure ());
		System.out.println (new_df.summary ());
		
		System.out.println ("=======Get Average Popilation of Egypt's Cities==============");
		String country_name = "france";
		int average_population = utili.get_average_population(country_name);
		System.out.println(average_population+ " is Average Popilation of " +country_name + "'s Cities");
		
		
		
		// CREATE SPARK CONTEXT
		//SparkConf conf = new SparkConf ().setAppName ("wordCounts").setMaster ("local[3]");
		//JavaSparkContext sparkContext = new JavaSparkContext (conf);
		
		
		
		SpringApplication.run(Hw8Application.class, args);
	}

}
