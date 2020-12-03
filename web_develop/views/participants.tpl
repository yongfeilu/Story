% include('header.tpl')
<!-- Main content should go here-->

<h1>Participants of {{film[0]}}</h1>

<table class="table table-striped">
    <tr>
    	<th>Professional ID</th>
    	<th>Name</th> 
    	<th>Gender</th>
    	<th>Date_Birth</th>
        <th>Country</th>
        <th>Occupation</th>
    </tr>
    % i = 0
    % for p in data:
    % i += 1
    
    
    <tr>
    	<td>{{p[0]}}</td>
    	<td>{{p[1]}}</td> 
    	<td>{{p[2]}}</td>
    	<td>{{p[3]}}</td>
        <td>{{p[4]}}</td>
        <td>{{p[5]}}</td>
    </tr>
    % end
</table>

	% if i == 0:
	<br>
	<h3>Oops! No participants recorded yet.</h3>
	% end

% include('footer.tpl')