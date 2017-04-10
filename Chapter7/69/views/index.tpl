<html>
<head>
  <meta charset="utf-8"/>
  <title>Artist Search</title>
</head>
<body>
  <h1>Artist Search</h1>
  <form action='/' method='POST' name='search_form'>
    <input type='text' name='name' placeholder='name'/></br>
    <input type='text' name='alias' placeholder='alias'/></br>
    <input type='text' name='tag' placeholder='tag'/></br>
    <input type='submit' value="search"/>
  </form>
{% if artists|length > 0 %}
  <table>
      <tr>
          <td>rating</td>
          <td>name</td>
          <td>aliase</td>
          <td>tag</td>
          <td>area</td>
          <td>begin</td>
          <td>end</td>
      </tr>
{% for artist in artists %}
      <tr>
          <td>artist.rating</td>
          <td>artist.name</td>
          <td>artist.aliase</td>
          <td>artist.tag</td>
          <td>artist.area</td>
          <td>artist.begin</td>
          <td>artist.end</td>
      </tr>
{% endfor %}
  </table>
{% endif %}
</body>
</html>
