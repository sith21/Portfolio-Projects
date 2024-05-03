-- Looking at some important data to get an idea of the table
SELECT location, date, total_cases, new_cases, total_deaths, population
FROM PortfolioProject..CovidDeaths$
WHERE continent is not null
ORDER by 1,2

-- Total Cases vs Total Deaths in Canada
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100  AS DeathsPercentage
FROM PortfolioProject..CovidDeaths$
WHERE continent is not null and location like '%canada%'
ORDER by 1,2


-- Total Cases vs Population in Canada
SELECT location, date, total_cases, population, (total_cases/population)*100  AS PopulationPercentage
FROM PortfolioProject..CovidDeaths$
WHERE continent is not null AND location like '%canada%'
ORDER by 1,2

-- Highest Infection Rates by Country Population

SELECT location, population, MAX(total_cases) AS  HighestInfectionCount, MAX((total_cases/population))*100  AS PopulationPercentageInfected
FROM PortfolioProject..CovidDeaths$
WHERE continent is not null
-- WHERE location like '%canada%'
GROUP BY location, population
ORDER by PopulationPercentageInfected DESC

-- Highest Death Rate by Country Population

SELECT location, population, MAX(cast(total_deaths as INT)) AS  TotalDeathCount, MAX((total_deaths/population))*100  AS PopulationPercentageDead
FROM PortfolioProject..CovidDeaths$
WHERE continent is not null
GROUP BY location, population
ORDER by TotalDeathCount DESC

-- Max Death Count By Country 

SELECT location, MAX(cast(total_deaths as INT)) AS  TotalDeathCount
FROM PortfolioProject..CovidDeaths$
WHERE continent is not null
GROUP BY location
ORDER by TotalDeathCount DESC

-- Max Death Count by Continent 

SELECT location, MAX(cast(total_deaths as INT)) AS  TotalDeathCount
FROM PortfolioProject..CovidDeaths$
WHERE continent is null
GROUP BY location
ORDER by TotalDeathCount DESC

-- Global Numbers Grouped by Date

SELECT date, SUM(new_cases) AS totalcases, SUM(cast(new_deaths as int)) AS totaldeaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100  AS DeathsPercentage
FROM PortfolioProject..CovidDeaths$
WHERE continent is not null
GROUP BY date
ORDER by 1,2

-- Global Numbers of Cases, Deaths, and Death Percentage

SELECT SUM(new_cases) AS totalcases, SUM(cast(new_deaths as int)) AS totaldeaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100  AS DeathsPercentage
FROM PortfolioProject..CovidDeaths$
WHERE continent is not null
--GROUP BY date
ORDER by 1,2

-- Using a CTE

With PopvsVac (Continent, Location, Date, Population, new_vaccinations, RollingPeopleVaccinated) 
AS
(
SELECT dea.continent, dea.location, dea.date, dea.population , vac.new_vaccinations, 
SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingPeopleVaccinated
FROM PortfolioProject..CovidDeaths$ as dea
JOIN PortfolioProject..CovidVaccinations$ as vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
-- ORDER BY 2,3
)

SELECT *, (RollingPeopleVaccinated/Population)*100 AS PercentageRollingVaccinations FROM PopvsVac

-- Temp Table

DROP Table if exists #PercentPopulationVaccinated -- To edit for new queries if needed
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_Vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert into #PercentPopulationVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population , vac.new_vaccinations, 
SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingPeopleVaccinated
FROM PortfolioProject..CovidDeaths$ as dea
JOIN PortfolioProject..CovidVaccinations$ as vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
ORDER BY 2,3
SELECT *, (RollingPeopleVaccinated/Population)*100 AS PercentageRollingVaccinations
FROM #PercentPopulationVaccinated

-- Creating View to store data for later visualizations

Create View PercentPopulationVaccinated AS
SELECT dea.continent, dea.location, dea.date, dea.population , vac.new_vaccinations, 
SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dea.location ORDER BY dea.location, dea.date) as RollingPeopleVaccinated
FROM PortfolioProject..CovidDeaths$ as dea
JOIN PortfolioProject..CovidVaccinations$ as vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null

SELECT * 
FROM PercentPopulationVaccinated
