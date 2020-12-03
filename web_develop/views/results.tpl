% include('header.tpl')
<!-- Main content should go here-->

<div class="container">

    <div style="width:80%;Text-align:left;float:left;">
        <h1>Movies</h1>
    </div>
    <br>
    <div style="Text-align:center;width:20%;float:right">
        <a href="/movies/add" class="btn btn-lg btn-success" style="margin-bottom: 12px">Add a New Movie</a>
    </div>
</div>

% if len(data) == 0:
<h3> There is no movie matching the conditions.</h3>
% end

<table class="table table-striped">
    <tr> 
    	<th>Film</th>
    	<th>Release Date</th>
    	<th>Language</th>
    	<th> </th>
    	<th> </th>
    	<th> </th>
    	<th> </th>
    </tr>

    % for movie in data:
    <tr>
    	<td>{{movie[1]}}</td>
    	<td>{{movie[2]}}</td>
    	<td>{{movie[4]}}</td>
    	<td> <a href="/movies/{{movie[0]}}">View / Edit</a> </td>
    	<td> <a href="/del/{{movie[0]}}">Delete</a></td> 
    	<td> <a href="/participants/{{movie[0]}}">Show participants</a></td>
    	<td> <a href="/participants/{{movie[0]}}/add">Add a new participant</a>
    </tr>
    % end

</table>

% include('footer.tpl')