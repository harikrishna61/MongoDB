/*
 * Team Members:
 * Rohit Katta (1001512896)
 * Harikrishna Bathala (1001415489)
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Driver;
using Newtonsoft.Json;
using System.Xml;

namespace XMLCreation
{
    class XMLCreator
    {
        protected static IMongoClient _client;
        protected static IMongoDatabase _database;

        static void Main(string[] args)
        {
            createProjectXML();
            Console.WriteLine();
            Console.WriteLine();
            createDepartmentXML();
            Console.ReadLine();
        }
        /// <summary>
        /// This method creates Project XML
        /// connects to mongodb, fetches all Project documents to a list
        /// For each item in list we convert that to XML string using JsonConvert.DeserializeXmlNode
        /// these individual xml nodes are added to blank xml document with projects as root node
        /// </summary>
        private static async void createProjectXML()
        {
            _client = new MongoClient(); //Creating client
            _database = _client.GetDatabase("project2"); //Connecting to database
            var collection = _database.GetCollection<BsonDocument>("project"); //Selecting collection
            var filter = new BsonDocument();
            var results = await collection.Find(filter).Project("{_id: 0}").ToListAsync(); //Fetching from MongoDb as a list of json strings
            XmlDocument doc = new XmlDocument();
            XmlNode rootNode = doc.CreateElement("projects"); //Blank XML Document with root node project
            doc.AppendChild(rootNode);
            foreach (var result in results) //Iterating over each JSON object
            {
                //Creating XML node with XML got by converting JSON, and adding node to XML Document
                XmlDocumentFragment proj = doc.CreateDocumentFragment();
                proj.InnerXml = JsonConvert.DeserializeXmlNode(result.ToJson(), "project").InnerXml;
                rootNode.AppendChild(proj);
            }
            Console.WriteLine(doc.OuterXml);
            doc.Save("project.xml"); // Saving Document
        }

        /// <summary>
        /// This method creates Project XML
        /// connects to mongodb, fetches all Department documents to a list
        /// For each item in list we convert that to XML string using JsonConvert.DeserializeXmlNode
        /// these individual xml nodes are added to blank xml document with documents as root node
        /// </summary>
        private static async void createDepartmentXML()
        {
            _client = new MongoClient(); //Creating client
            _database = _client.GetDatabase("project2"); //Connecting to database
            var collection = _database.GetCollection<BsonDocument>("department"); //Selecting collection
            var filter = new BsonDocument();
            var results = await collection.Find(filter).Project("{_id: 0}").ToListAsync(); //Fetching from MongoDb as a list of json strings
            XmlDocument doc = new XmlDocument();
            XmlNode rootNode = doc.CreateElement("departments"); //Blank XML Document with root node departments
            doc.AppendChild(rootNode);
            foreach (var result in results) //Iterating over each JSON object
            {
                //Creating XML node with XML got by converting JSON, and adding node to XML Document
                XmlDocumentFragment proj = doc.CreateDocumentFragment();
                proj.InnerXml = JsonConvert.DeserializeXmlNode(result.ToJson(), "department").InnerXml;
                rootNode.AppendChild(proj);
            }
            Console.WriteLine(doc.OuterXml);
            doc.Save("department.xml");
        }
    }
}
