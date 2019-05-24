/**
 * 
 */
package br.ufrn.deeplearning.logprocess;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import br.ufrn.deeplearning.util.CSVUtils;

/**
 * Read the log file to generated the test database and generated the input format for the deep learning
 * 
 * @author jadson
 *
 */
public class ExtractTestSetFromLogInformation {

	public final static String TEST_DATA_DIRECTORY = "/Users/jadson/Desktop/conjunto_de_teste/1/";
	
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		prepareTestSet();
	}

	
	
	/**
	 * Prepare the test set
	 * 
	 * genarate the xtest and ytest files
	 * 
	 * @throws FileNotFoundException
	 * @throws IOException
	 */
	public static void prepareTestSet() throws FileNotFoundException, IOException {
		
		List<LineInformation> lines = new ArrayList<>();
		
		String logFileName = TEST_DATA_DIRECTORY+"log_operacao_criar_evento_1.log";
		String csvFile = TEST_DATA_DIRECTORY+"xtest_0_1.csv";
		
//		String logFileName = TEST_DATA_DIRECTORY+"log_operacao_abrir_periodo_submissao.log";
//		String csvFile = TEST_DATA_DIRECTORY+"xtest_0_2.csv";
		
//		String logFileName = TEST_DATA_DIRECTORY+"log_operacao_abrir_periodo_inscricao.log";
//		String csvFile = TEST_DATA_DIRECTORY+"xtest_0_3.csv";
//		
//		String logFileName = TEST_DATA_DIRECTORY+"log_operacao_cadastrar_programacao.log";
//		String csvFile = TEST_DATA_DIRECTORY+"xtest_0_4.csv";
//		
//		String logFileName = TEST_DATA_DIRECTORY+"log_operacao_cadastrar_palestrante.log";
//		String csvFile = TEST_DATA_DIRECTORY+"xtest_0_5.csv";
//		
//		String logFileName = TEST_DATA_DIRECTORY+"log_operacao_distribuir_trabalho_automaticamente.log";
//		String csvFile = TEST_DATA_DIRECTORY+"xtest_0_6.csv";
//		
//		String logFileName = TEST_DATA_DIRECTORY+"log_operacao_pagina_publica_evento.log";
//		String csvFile = TEST_DATA_DIRECTORY+"xtest_0_7.csv";
//		
//		String logFileName = TEST_DATA_DIRECTORY+"log_operacao_realizar_avaliacao.log";
//		String csvFile = TEST_DATA_DIRECTORY+"xtest_0_8.csv";
//		
//		String logFileName = TEST_DATA_DIRECTORY+"log_operacao_submeter_trabalho.log";
//		String csvFile = TEST_DATA_DIRECTORY+"xtest_0_9.csv";
//		
//		String logFileName = TEST_DATA_DIRECTORY+"log_operacao_inscrever_evento.log";
//		String csvFile = TEST_DATA_DIRECTORY+"xtest_0_10.csv";
		
		try(BufferedReader br = new BufferedReader(new FileReader(logFileName))) {
		    String line = br.readLine();

		    while (line != null) {
		        lines.add( splitLogOperacao(line) );
		        line = br.readLine();
		    }
		    
		}
		
		
        FileWriter writer = new FileWriter(csvFile);

        for (LineInformation lineInformation : lines) {
        		CSVUtils.writeLine(writer, Arrays.asList(lineInformation.url));
		}
        
        writer.flush();
        writer.close();
		
	}
	
	/**
	 * line = "2018-06-20 18:41:21,699 598ec325-1db0-41b8-a658-116de65f0f4c e9fb8268-7340-4d83-92b2-cc1aafcf5c50 INFO  [br.ufrn.arq.seguranca.log.LogOperacao] 2018-06-20T18:41:21.0699Z http://localhost:8080/eventos/interno/menu.xhtml 33 16 172661858   false  {\"formMenuPrincipal:tabView:formCalendarioEventos:j_idt193_view\":[\"month\"],\"javax.faces.ViewState\":[\"-9042878530288200042:-2780710332792365200\"],\"formMenuPrincipal:tabView_tabindex\":[\"2\"],\"javax.faces.partial.execute\":[\"formMenuPrincipal:tabView\"],\"formMenuPrincipal:tabView_activeIndex\":[\"2\"],\"formMenuPrincipal:tabView:tabViewRelatorios_activeIndex\":[\"0\"],\"formMenuPrincipal:tabView_newTab\":[\"formMenuPrincipal:tabView:tab3\"],\"javax.faces.partial.event\":[\"tabChange\"],\"javax.faces.behavior.event\":[\"tabChange\"],\"javax.faces.partial.ajax\":[\"true\"],\"javax.faces.source\":[\"formMenuPrincipal:tabView\"],\"formMenuPrincipal\":[\"formMenuPrincipal\"],\"formMenuPrincipal:tabView:formCalendarioEventos\":[\"formMenuPrincipal:tabView:formCalendarioEventos\"]}";
	 * @param line
	 * @return
	 */
	public static LineInformation splitLogOperacao(String line) {
		
		String[] values = line.split(" ");
		
		return new LineInformation(values[7], values[8], values[9], values[10], values[11], values[16] );
		
	}
	
	
	
	
}

class LineInformation {
	

	String timeStamp;
	String url;
	Integer time;
	Integer systemId;
	Long userSessionId;
	String parameter;
	
	public LineInformation(String timeStamp, String url, String time, String systemId, String userSessionId, String parameter) {
		this.timeStamp = timeStamp;
		this.url = url;
		this.time = new Integer(time);
		this.systemId = new Integer(systemId);
		this.userSessionId = new Long(userSessionId);
		this.parameter = parameter;
	}

	@Override
	public String toString() {
		return "LineInformation [timeStamp=" + timeStamp + ", url=" + url + ", time=" + time + ", systemId=" + systemId
				+ ", userSessionId=" + userSessionId + ", parameter=" + parameter + "]";
	}
	
}


