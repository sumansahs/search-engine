import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import { Pagination, Spin, Input, Card, Tooltip, Layout } from 'antd';

const { Search } = Input;
const { Header, Content } = Layout;

function App() {
  const [query, setQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [imageResults, setImageResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);

  const handleSearch = async (value) => {
    setLoading(true);
    try {
      const response = await axios.get(`http://127.0.0.1:5000/search?query=${value}`);
      setSearchResults(response.data.search_results);
      setImageResults(response.data.image_results);
    } catch (error) {
      console.error('Error fetching search results:', error);
    } finally {
      setLoading(false);
    }
  };

  const onPageChange = (page) => {
    setCurrentPage(page);
  };

  const resultsPerPage = 10;
  const paginatedSearchResults = searchResults.slice((currentPage - 1) * resultsPerPage, currentPage * resultsPerPage);
  const paginatedImageResults = imageResults.slice((currentPage - 1) * resultsPerPage, currentPage * resultsPerPage);

  return (
    <Layout className="App">
      <Header className="App-header">
        <h1>Search Engine</h1>
        <Search
          placeholder="Enter your query..."
          enterButton="Search"
          size="large"
          onSearch={handleSearch}
          onChange={(e) => setQuery(e.target.value)}
          value={query}
          style={{ maxWidth: 600, margin: '20px auto' }}
        />
      </Header>

      <Content className="results-container">
        {loading ? (
          <Spin size="large" />
        ) : (
          <>
            <div className="search-results">
              <h2>Text Results</h2>
              {paginatedSearchResults.map((result, index) => (
                <Card
                  key={index}
                  title={
                    <Tooltip title={result.snippet}>
                      <a href={result.link} target="_blank" rel="noopener noreferrer">
                        {result.title}
                      </a>
                    </Tooltip>
                  }
                  style={{ marginBottom: 20 }}
                >
                  <p>{result.snippet}</p>
                </Card>
              ))}
            </div>

            <div className="image-results">
              <h2>Image Results</h2>
              <div className="image-grid">
                {paginatedImageResults.map((image, index) => (
                  <Card key={index} hoverable cover={<img alt="search result" src={image.src} />} />
                ))}
              </div>
            </div>

            <Pagination
              current={currentPage}
              total={Math.max(searchResults.length, imageResults.length)}
              pageSize={resultsPerPage}
              onChange={onPageChange}
              style={{ textAlign: 'center', marginTop: 20 }}
            />
          </>
        )}
      </Content>
    </Layout>
  );
}

export default App;
