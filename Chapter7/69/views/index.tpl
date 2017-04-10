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
  <table border=1>
      <tr>
          <td>レーティング</td>
          <td>名前</td>
          <td>別名</td>
          <td>タグ情報</td>
      </tr>
{% for artist in artists %}
      <tr>
          <td>{{ artist.rating_value }}</td>
          <td>{{ artist.name }}</td>
          <td>{{ artist.aliases_name |join(", ") }}</td>
          <td>{{ artist.tags_value |join(", ") }}</td>
      </tr>
{% endfor %}
  </table>
{% endif %}
</body>
</html>
