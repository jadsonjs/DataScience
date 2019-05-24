/**
 * 
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
 * STEP 2
 * 
 * This class generate the output, or labels ou y_train data set by a heuristic
 * 
 * @author jadson
 *
 */
public class GenerateOutDataSet {
	
	//public final static String DEFAULT_DIRECTORY         = "/Users/jadson/git/deeplearning/data/";
	public final static String DEFAULT_DIRECTORY             = "/home/jadson/git/deeplearning/data/";
	public final static String TRAINING_DATA_DIRECTORY       = DEFAULT_DIRECTORY+"training/";
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
		
		
		List<String> urls = new ArrayList<String>();
		
		
		////////////////// for training data  ////////////////// 
		forfiles:
		for (int i = 1; i < 1000000; i++) {
			String csvFile = TRAINING_DATA_DIRECTORY+"training_"+i+".csv";
			
			String csvOutFile = TRAINING_DATA_DIRECTORY+"y_training_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				
				Float[] y = new Float[10]; // value of output of 10 classes
				
				for (int f = 0; f < y.length; f++) {
					y[f] = 0f;
				}
				
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
				    String line = br.readLine();
		
				    while (line != null) {
				    	urls.add( line );
				        line = br.readLine();
				    }
				    
				    
				    // END ALL LINES
				    
				    applyHeuristic(urls, y);
				    
				    saveOutPutFile(csvOutFile, y);
				    
				    urls = new ArrayList<String>();
				    
				}	
				
			}else {
				break forfiles;
			}
		}
		
		forfiles:
			for (int i = 1; i < 1000000; i++) {
				String csvFile = TEST_DATA_DIRECTORY+"test_"+i+".csv";
				
				String csvOutFile = TEST_DATA_DIRECTORY+"y_test_"+i+".csv";
				
				File file = new File(csvFile);
				
				if( file.exists() ) {
					
					Float[] y = new Float[10]; // value of output of 10 classes
					
					for (int f = 0; f < y.length; f++) {
						y[f] = 0f;
					}
					
					FileReader fileReader = new FileReader(file);
					
					try(   BufferedReader br = new BufferedReader(fileReader)  ) {
						
					    String line = br.readLine();
			
					    while (line != null) {
					    	urls.add( line );
					        line = br.readLine();
					    }
					    
					    
					    // END ALL LINES
					    
					    applyHeuristic(urls, y);
					    
					    saveOutPutFile(csvOutFile, y);
					    
					    urls = new ArrayList<String>();
					    
					}	
					
				}else {
					break forfiles;
				}
			}
		
		
		forfiles:
			for (int i = 201; i < 1000000; i++) {
				String csvFile = VALIDATION_DATA_DIRECTORY+"test_"+i+".csv";
				
				String csvOutFile = VALIDATION_DATA_DIRECTORY+"y_test_"+i+".csv";
				
				File file = new File(csvFile);
				
				if( file.exists() ) {
					
					Float[] y = new Float[10]; // value of output of 10 classes
					
					for (int f = 0; f < y.length; f++) {
						y[f] = 0f;
					}
					
					FileReader fileReader = new FileReader(file);
					
					try(   BufferedReader br = new BufferedReader(fileReader)  ) {
						
					    String line = br.readLine();
			
					    while (line != null) {
					    	urls.add( line );
					        line = br.readLine();
					    }
					    
					    
					    // END ALL LINES
					    
					    applyHeuristic(urls, y);
					    
					    saveOutPutFile(csvOutFile, y);
					    
					    urls = new ArrayList<String>();
					    
					}	
					
				}else {
					break forfiles;
				}
			}
		
	}

	
	/**
	 * Apply Heuristic to try to determinate the output for the 100 urls sequence.
	 * 
	 * 1. Create new Event
     * 2. Open Submission Period
	 * 3. Open Subscription Period
	 * 4. Create programming
	 * 5. Create Keynotes
	 * 6. Distribute Submission
	 * 7. Create Event Page
	 * 8. Perform Evaluation
	 * 9. Make Submission
	 * 10. Make Subscription
	 * 
	 * @param urls
	 * @param y
	 */
	private static void applyHeuristic(List<String> urls, Float[] y) {
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/cadastros/eventos/formCadastraAlteraEvento.xhtml") ) {
			y[0] += 0.5f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/cadastros/eventos/formCadastraAlteraDadosEventoPrincipal.xhtml") ) {
			y[0] += 0.5f;
		}
		
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/cadastros/eventos/listaPeriodosDeSubmissaoEvento.xhtml") ) {
			y[1] += 0.3f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/cadastros/eventos/formPeriodosDeSubmissaoEvento.xhtml") ) {
			y[1] += 0.5f;
		}
		
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/cadastros/eventos/formPeriodosDeInscricaoEvento.xhtml") ) {
			y[2] += 0.5f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/cadastros/eventos/listaPeriodosDeInscricaoEvento.xhtml") ) {
			y[2] += 0.5f;
		}
		
		//Create programming
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/locais_apresentacao/listaLocaisApresentacaoTrabalho.xhtml") ) {
			y[3] += 0.3f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/locais_apresentacao/formLocaisApresentacaoTrabalho.xhtml") ) {
			y[3] += 0.5f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/pesquisas/buscaPadraoEventos.xhtml") ) {
			y[3] += 0.1f;
		}
		
		//  Create Keynotes
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/palestrantes/formCadastraPalestranteEvento.xhtml") ) {
			y[4] += 0.5f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/palestrantes/listaPalestrantesGerenciar.xhtml") ) {
			y[4] += 0.3f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/pesquisas/buscaPadraoEventos.xhtml") ) {
			y[4] += 0.1f;
		}
		
		// Distribute Submission
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/avaliacoes/distribuicao/formDistribuiSubmissoes.xhtml") ) {
			y[5] += 0.5f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/cadastros/permissoes/cadastraPermissoesPessoaSelecionada.xhtml") ) {
			y[5] += 0.1f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/cadastros/permissoes/listaPermissoesPessoaSelecionada.xhtml") ) {
			y[5] += 0.1f;
		}
		
		// Create Event Page
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/paginaPublicaEvento/formConfiguracoesPaginaPublica.xhtml") ) {
			y[6] += 0.7f;
		}
	
		//  Perform Evaluation
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/avaliacoes/parciais/formAvaliacaoParcial.xhtml") ) {
			y[7] += 0.5f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/avaliacoes/parciais/listaMinhasAvaliacoes.xhtml") ) {
			y[7] += 0.3f;
		}
		
		// Make Submission
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/submissoes/formSubmeterTrabalho.xhtml") ) {
			y[8] += 0.5f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/submissoes/listaMinhasSubmissoes.xhtml") ) {
			y[8] += 0.3f;
		}
		
		// Make Subscription
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/inscricoes/formInscreveseEvento.xhtml") ) {
			y[9] += 0.5f;
		}
		if( urls.contains("http://www.sigeventos.ufrn.br/eventos/interno/inscricoes/listaMinhasIncricoes.xhtml") ) {
			y[9] += 0.3f;
		}
		
	}

	private static void saveOutPutFile(String csvOutFile, Float[] y) throws IOException {
		// save the mapping to return //
		
		
		FileWriter writer = new FileWriter(csvOutFile);

		StringBuilder builder = new StringBuilder();
		for (int i = 0; i < y.length; i++) {
			if(i < y.length-1)
				builder.append(y[i]+";");
			else
				builder.append(y[i]);
		}
		CSVUtils.writeLine(writer, Arrays.asList( builder.toString() )  );
        
        writer.flush();
        writer.close();
	}

	
	
}
