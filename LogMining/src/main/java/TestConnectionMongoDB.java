import com.mongodb.MongoClient;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.MongoIterable;

/**
 * 
 */

/**
 * @author jadson
 *
 */
public class TestConnectionMongoDB {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		testWriteInformationIntoMongoDB();
	}
	
	/**
	 * Write information in an NoSQL database
	 * @param data
	 */
	protected static void testWriteInformationIntoMongoDB() {
	
		
		MongoClient mongoClient = null;
		
		try {

			mongoClient = new MongoClient("mongodbserver", 27017);
			
			
			MongoIterable<String> databases = mongoClient.listDatabaseNames();
            
            for (String dbName : databases) {
                System.out.println("- Database: " + dbName);
                 
                MongoDatabase db = mongoClient.getDatabase(dbName);
                 
                MongoIterable<String> collections = db.listCollectionNames();
                for (String colName : collections) {
                    System.out.println("\t + Collection: " + colName);
                }
            }
			
		}finally{
			mongoClient.close();
		}
	}

}
