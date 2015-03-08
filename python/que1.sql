select country.name, island_province, total_islands from country inner join 
(select distinct total_islands,GEO_ISLAND.COUNTRY as country_code, GEO_ISLAND.PROVINCE as island_province 
	from GEO_ISLAND inner join (select count(*) as total_islands, province as p from GEO_ISLAND group by province) 
	on GEO_ISLAND.PROVINCE = p where total_islands = (select max(count(*)) from GEO_ISLAND group by province)) 
on country.CODE = country_code;


select * from (
	select name, population*power(1+p.population_growth,5) as future_population, rank() over (
		order by population*power(1+p.population_growth,5) desc) as rank from country c, population p 
	where c.code = p.country and p.population_growth is not null order by rank) where rank <=5 ;

select c.name, e.GDP from country c, economy e where c.code = e.country and 
code in (select country from ismember where ORGANIZATION = 'NATO') and 
code in (select country from religion where name = 'Muslim' and PERCENTAGE>= 5);


select country_name, language_name,PERCENTAGE from (
	select c.name country_name, l.name as language_name, l.PERCENTAGE as PERCENTAGE from country c, language l where 
	c.CODE = l.COUNTRY and l.PERCENTAGE = (select max(ll.PERCENTAGE) from language ll where ll.country = c.CODE)) 
inner join (select name as l_name from (
	select l.name name ,sum(l.percentage*c.population) as speakers from country c, language l where 
	c.CODE = l.COUNTRY group by l.NAME) where speakers > 50000000) on l_name = language_name;