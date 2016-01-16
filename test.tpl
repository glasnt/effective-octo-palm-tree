<html>
<head>
<body>
<h1>HatRack for {{result["repo"]}}</h1>

Non Code Contributions
<ul>
%for c in result["non"]:
  <li>{{c["name"]}}
%end
</ul>
<br>
<br>
Code Contributions
<ul>
%for c in result["con"]:
  <li>{{c["name"]}}
%end
</ul>
<br>
Commentor statistics aggregated from the most recent {{result["limit"]}} issues and PRs. 
