package hw8.hw8;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RestClass {
	
	Utilis util = new Utilis();
	
	
	@RequestMapping("/countrypouplation")
	public String helloname(@RequestParam(value="name", defaultValue = "egypt") String country_name) {
		int average_population = util.get_average_population(country_name);
		return "Average Population of " + country_name + "\'s Cities is " + average_population; 
	}

}
