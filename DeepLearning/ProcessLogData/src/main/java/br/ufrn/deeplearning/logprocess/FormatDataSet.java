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
 * RemoveDoubleQuotes.java 
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
import java.util.List;

import br.ufrn.deeplearning.util.CSVUtils;

/**
 * STEP 1
 * 
 * remove " from "url" and replece for sema url
 * 
 * @author Jadson Santos - jadsonjs@gmail.com
 *
 */
public class FormatDataSet {

	public final static String DEFAULT_DIRECTORY = "/home/jadson/git/deeplearning/data/";
	
	public final static String TRAINING_DATA_DIRECTORY       = DEFAULT_DIRECTORY+"training/";
	public final static String TEST_DATA_DIRECTORY           = DEFAULT_DIRECTORY+"tests/";
	public final static String VALIDATION_DATA_DIRECTORY     = DEFAULT_DIRECTORY+"validation/";
	
	/**
	 * @param args
	 * @throws IOException 
	 * @throws FileNotFoundException 
	 */
	public static void main(String[] args) throws FileNotFoundException, IOException {
		
		forfiles:
		for (int i = 1; i < 1000000; i++) {
			
			String csvFile = TRAINING_DATA_DIRECTORY+"training_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				
				System.out.println("treating file: "+csvFile);
				
				List<String> lines = new ArrayList<>();
				
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
				    String line = br.readLine();
		
				    while (line != null) {
				    	line = formatURL(line);
				        lines.add( line );
				        line = br.readLine();
				    }
				}	
				
				FileWriter writer = new FileWriter(csvFile);
		
		        for (String line : lines) {
		        		CSVUtils.writeLine(writer, Arrays.asList(line));
				}
		        
		        writer.flush();
		        writer.close();
		        
			}else {
				System.out.println("end no more files ");
				break forfiles;
			}
		}
	
	
		forfiles:
		for (int i = 1; i < 1000000; i++) {
			
			String csvFile = TEST_DATA_DIRECTORY+"test_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				
				System.out.println("treating file: "+csvFile);
				
				List<String> lines = new ArrayList<>();
				
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
				    String line = br.readLine();
		
				    while (line != null) {
				    	line = formatURL(line);
				        lines.add( line );
				        line = br.readLine();
				    }
				}	
				
				FileWriter writer = new FileWriter(csvFile);
		
		        for (String line : lines) {
		        		CSVUtils.writeLine(writer, Arrays.asList(line));
				}
		        
		        writer.flush();
		        writer.close();
		        
			}else {
				System.out.println("end no more files ");
				break forfiles;
			}
		}
		
		
		forfiles:
			for (int i = 201; i < 1000000; i++) {
				
				String csvFile = VALIDATION_DATA_DIRECTORY+"test_"+i+".csv";
				
				File file = new File(csvFile);
				
				if( file.exists() ) {
					
					System.out.println("treating file: "+csvFile);
					
					List<String> lines = new ArrayList<>();
					
					FileReader fileReader = new FileReader(file);
					
					try(   BufferedReader br = new BufferedReader(fileReader)  ) {
						
					    String line = br.readLine();
			
					    while (line != null) {
					    	line = formatURL(line);
					        lines.add( line );
					        line = br.readLine();
					    }
					}	
					
					FileWriter writer = new FileWriter(csvFile);
			
			        for (String line : lines) {
			        		CSVUtils.writeLine(writer, Arrays.asList(line));
					}
			        
			        writer.flush();
			        writer.close();
			        
				}else {
					System.out.println("end no more files ");
					break forfiles;
				}
			}
	
		
	}
	
	
//	int sample = 1; // unfortunately just for 1 sample
//	
//	for (int operation = 1; operation <= 10; operation++) {
//		
//		String csvFile = TEST_DATA_DIRECTORY+"xtest_"+sample+"_"+operation+".csv";
//		
//		System.out.println("treating file: "+csvFile);
//		
//		List<String> lines = new ArrayList<>();
//		
//		try( BufferedReader br = new BufferedReader(new FileReader(csvFile))  ) {
//			String line = br.readLine();
//
//		    while (line != null) {
//		    	line = formatURL(line);
//		        lines.add( line );
//		    	line = br.readLine();
//		    }
//		}
//		
//		FileWriter writer = new FileWriter(csvFile);
//		
//        for (String line : lines) {
//        		CSVUtils.writeLine(writer, Arrays.asList(line));
//		}
//        
//        writer.flush();
//        writer.close();
//	}
	
	

	private static String formatURL(String line) {
		line = line.replaceAll("\"", "");  // remove '"'
		line = line.replaceAll("https://www.sigeventos.ufrn.br/", "http://www.sigeventos.ufrn.br/");
		line = line.replaceAll("https://sigeventos.ufrn.br/",     "http://www.sigeventos.ufrn.br/");
		line = line.replaceAll("http://sigeventos.ufrn.br/",      "http://www.sigeventos.ufrn.br/");
		line = line.replaceAll("http://localhost:8080/",          "http://www.sigeventos.ufrn.br/");
		return line;
	}

}
