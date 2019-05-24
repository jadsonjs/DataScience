/*
 * Copyright (c) 2017 Jadson Santos
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 * NormalizeUrls.java 
 * 27 de jun de 2018
 */
package br.ufrn.deeplearning.logprocess;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import br.ufrn.deeplearning.util.CSVUtils;

/**
 * STEP 3
 * 
 * 3 normalize data of traning, test and validation
 * 
 * change all url by numbers
 * 
 * @author Jadson Santos - jadsonjs@gmail.com
 *
 */
public class NormalizeDataSet {
	
	public final static String DEFAULT_DIRECTORY       = "/home/jadson/git/deeplearning/data/";
	public final static String TRAINING_DATA_DIRECTORY        = DEFAULT_DIRECTORY+"training/";
	public final static String TEST_DATA_DIRECTORY           = DEFAULT_DIRECTORY+"tests/";
	public final static String VALIDATION_DATA_DIRECTORY     = DEFAULT_DIRECTORY+"validation/";
	
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		normalizeData();
	}

	/**
	 * Generate a number form each URL
	 * 
	 * @throws IOException
	 * @throws FileNotFoundException
	 */
	private static void normalizeData() throws IOException, FileNotFoundException {
		
		Set<String> distinctUrls = new HashSet<String>();
		
		////////////////// for training data  ////////////////// 
		forfiles:
		for (int i = 1; i < 1000000; i++) {
			String csvFile = TRAINING_DATA_DIRECTORY+"training_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
				    String line = br.readLine();
		
				    while (line != null) {
				    		distinctUrls.add( line );
				        line = br.readLine();
				    }
				}	
				
			}else {
				break forfiles;
			}
		}

		//////////////////for test data  //////////////////
		forfiles:
		for (int i = 1; i < 1000000; i++) {
			String csvFile = TEST_DATA_DIRECTORY+"test_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
				    String line = br.readLine();
		
				    while (line != null) {
				    		distinctUrls.add( line );
				        line = br.readLine();
				    }
				}	
				
			}else {
				break forfiles;
			}
		}
		
		//////////////////for validation data  //////////////////
		forfiles:
		for (int i = 201; i < 1000000; i++) {
			String csvFile = VALIDATION_DATA_DIRECTORY+"test_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
				    String line = br.readLine();
		
				    while (line != null) {
				    		distinctUrls.add( line );
				        line = br.readLine();
				    }
				}	
				
			}else {
				break forfiles;
			}
		}
				
		
		
		List<String> distinctUrlsList = new ArrayList<String>(distinctUrls);		
		List<Integer> urlsNumberList = genaratedSequencialNumber(distinctUrlsList);
		
		
		
		saveMapingFile(distinctUrlsList, urlsNumberList);
        
        
		/////////    change the url texto to numeric value for training data ///////
		
		forfiles:
		for (int i = 1; i < 1000000; i++) {
			String csvFile = TRAINING_DATA_DIRECTORY+"training_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				
				FileWriter finalWriter = new FileWriter(  TRAINING_DATA_DIRECTORY+"training_norm_"+i+".csv" );
				
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
					String line = br.readLine();

				    while (line != null) {
				    		int index = distinctUrlsList.indexOf((line));
				    		
				    		int urlNumber = urlsNumberList.get(index);
				    		
			    	        	CSVUtils.writeLine(finalWriter, Arrays.asList( ""+urlNumber)  );
				    		line = br.readLine();
				    }
				    
				}
				
				finalWriter.flush();
				finalWriter.close();
				
			}else {
				break forfiles;
			}
		}
		
        
		/////////    change the url texto to numeric value for test data ///////
		
		forfiles:
		for (int i = 1; i < 1000000; i++) {
			String csvFile = TEST_DATA_DIRECTORY+"test_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				
				FileWriter finalWriter = new FileWriter(  TEST_DATA_DIRECTORY+"test_norm_"+i+".csv" );
				
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
					String line = br.readLine();

				    while (line != null) {
				    		int index = distinctUrlsList.indexOf((line));
				    		
				    		int urlNumber = urlsNumberList.get(index);
				    		
			    	        	CSVUtils.writeLine(finalWriter, Arrays.asList( ""+urlNumber)  );
				    		line = br.readLine();
				    }
				    
				}
				
				finalWriter.flush();
				finalWriter.close();
				
			}else {
				break forfiles;
			}
		}
		
		
		/////////    change the url texto to numeric value for validion data ///////
		
		forfiles:
		for (int i = 201; i < 1000000; i++) {
			String csvFile = VALIDATION_DATA_DIRECTORY+"test_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				
				FileWriter finalWriter = new FileWriter(  VALIDATION_DATA_DIRECTORY+"test_norm_"+i+".csv" );
				
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
					String line = br.readLine();

				    while (line != null) {
				    		int index = distinctUrlsList.indexOf((line));
				    		
				    		int urlNumber = urlsNumberList.get(index);
				    		
			    	        	CSVUtils.writeLine(finalWriter, Arrays.asList( ""+urlNumber)  );
				    		line = br.readLine();
				    }
				    
				}
				
				finalWriter.flush();
				finalWriter.close();
				
			}else {
				break forfiles;
			}
		}
		
	}

	private static void saveMapingFile(List<String> distinctUrlsList, List<Integer> urlsNumberList) throws IOException {
		// save the mapping to return //
		String csvFile = DEFAULT_DIRECTORY+"urls_maps.csv";
		
		FileWriter writer = new FileWriter(csvFile);

		for (int i = 0; i < distinctUrlsList.size(); i++) {
        		CSVUtils.writeLine(writer, Arrays.asList( ""+distinctUrlsList.get(i), ""+urlsNumberList.get(i))  );
		}
        
        writer.flush();
        writer.close();
	}

	private static List<Integer> genaratedSequencialNumber(List<String> distinctUrlsList) {
		List<Integer> urlsNumberList = new ArrayList<Integer>(distinctUrlsList.size());
		
		int number = 1;
		for (int i = 0; i < distinctUrlsList.size(); i++) {
			urlsNumberList.add(number++);
		}
		return urlsNumberList;
	}
	
	
}
