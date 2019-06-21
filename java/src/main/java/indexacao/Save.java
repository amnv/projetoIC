package indexacao;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.List;

import org.apache.lucene.document.Document;

public class Save {
	public void buildDocument(String docName) throws Exception {
		Search sc = new Search();
		List<Document> docs = sc.searchDocuments(docName);// replicar metodo
		// Olhar metodos da classe Document
		if (docs.size() > 0) {
			BufferedWriter writer = null;
			try {
				File file = new File("../results/seed/novos2/" + docName + ".txt");

				// This will output the full path where the file will be written to...
				System.out.println(file.getCanonicalPath());

				writer = new BufferedWriter(new FileWriter(file));
				for (int i = 0; i < docs.size(); i++) {
					writer.write(docs.get(i).get("contents"));
					writer.write("\n");
				}
			} catch (Exception e) {
				e.printStackTrace();
			} finally {
				try {
					// Close the writer regardless of what happens...
					writer.close();
				} catch (Exception e) {
				}
			}
		} else
			System.out.println("Está consulta não teve resultados");
	}

	public void saveFromList() throws Exception {
		String[] toSearch = new String[] {
				"Bone Marrow",
				"Adipose Tissue",
				"Umbilical Cord",
		};
		
		for (String queryString : toSearch) 
		{
			buildDocument(queryString);
		}
	}

	public void saveFromFile() throws Exception {
		String[] toSearch = new String[] {
				"neuronal receptor cell",
				"early embryonic cell",
				"neuroplacodal cell",
				"apocrine cell",
				"stem cell", 
				"totipotent stem cell",
				"bone matrix secreting cell",
				"ameloblast",
				"odontoblast",
				"cementoblast",
				"osteoblast",
				"neural cell",
				"precursor cell",
				"kidney cell",
				"myoblast",
				"fibroblast",
				"epithelial cell"
		};
		
		for (String queryString : toSearch) 
		{
			buildDocument(queryString);
		}
	}
}
