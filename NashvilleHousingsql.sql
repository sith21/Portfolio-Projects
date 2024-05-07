SELECT TOP (1000) [UniqueID ]
      ,[ParcelID]
      ,[LandUse]
      ,[PropertyAddress]
      ,[SaleDate]
      ,[SalePrice]
      ,[LegalReference]
      ,[SoldAsVacant]
      ,[OwnerName]
      ,[OwnerAddress]
      ,[Acreage]
      ,[TaxDistrict]
      ,[LandValue]
      ,[BuildingValue]
      ,[TotalValue]
      ,[YearBuilt]
      ,[Bedrooms]
      ,[FullBath]
      ,[HalfBath]
  FROM [PortfolioProject].[dbo].[NashvilleHousingDatabase]

   -- Standardize Date Format

SELECT *
FROM PortfolioProject..NashvilleHousingDatabase

ALTER TABLE PortfolioProject..NashvilleHousingDatabase
ALTER COLUMN SaleDate DATE

SELECT SaleDate
FROM PortfolioProject..NashvilleHousingDatabase

SELECT *
FROM PortfolioProject..NashvilleHousingDatabase


-- Populate Property Address Data

SELECT * 
FROM PortfolioProject..NashvilleHousingDatabase
WHERE PropertyAddress is null
ORDER BY ParcelID

SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM PortfolioProject..NashvilleHousingDatabase a
JOIN PortfolioProject..NashvilleHousingDatabase b
	ON a.ParcelID = b.ParcelID
	AND a. [UniqueID] <> b.[UniqueID] 
WHERE a.PropertyAddress is null

UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM PortfolioProject..NashvilleHousingDatabase a
JOIN PortfolioProject..NashvilleHousingDatabase b
	ON a.ParcelID = b.ParcelID
	AND a. [UniqueID] <> b.[UniqueID] 
WHERE a.PropertyAddress is null




-- Breaking out Address into Individual Columns (Address, City, State)
SELECT PropertyAddress
FROM PortfolioProject..NashvilleHousingDatabase --delimeter after address

SELECT
SUBSTRING(PropertyAddress,1,CHARINDEX(',',PropertyAddress)-1) as Address,
SUBSTRING(PropertyAddress,CHARINDEX(',',PropertyAddress)+1,LEN(PropertyAddress)) as City
FROM PortfolioProject..NashvilleHousingDatabase

ALTER TABLE PortfolioProject..NashvilleHousingDatabase
DROP COLUMN PropertySplitCity

ALTER TABLE PortfolioProject..NashvilleHousingDatabase
ADD PropertySplitAddress Nvarchar(255)

UPDATE NashvilleHousingDatabase
SET PropertySplitAddress = SUBSTRING(PropertyAddress,1,CHARINDEX(',',PropertyAddress)-1)


ALTER TABLE PortfolioProject..NashvilleHousingDatabase
ADD PropertySplitCity Nvarchar(255)

UPDATE NashvilleHousingDatabase
SET PropertySplitCity = SUBSTRING(PropertyAddress,CHARINDEX(',',PropertyAddress)+1,LEN(PropertyAddress))

SELECT *
FROM PortfolioProject..NashvilleHousingDatabase


SELECT
PARSENAME(REPLACE(OwnerAddress,',','.'),3),
PARSENAME(REPLACE(OwnerAddress,',','.'),2),
PARSENAME(REPLACE(OwnerAddress,',','.'),1)
FROM PortfolioProject..NashvilleHousingDatabase

ALTER TABLE PortfolioProject..NashvilleHousingDatabase
ADD OwnerSplitAddress Nvarchar(255)

UPDATE NashvilleHousingDatabase
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress,',','.'),3)

ALTER TABLE PortfolioProject..NashvilleHousingDatabase
ADD OwnerSplitCity Nvarchar(255)

UPDATE NashvilleHousingDatabase
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress,',','.'),2)

ALTER TABLE PortfolioProject..NashvilleHousingDatabase
ADD OwnerSplitState Nvarchar(255)

UPDATE NashvilleHousingDatabase
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress,',','.'),1)

SELECT *
FROM PortfolioProject..NashvilleHousingDatabase


-- Change SoldAsVacant From Yes/No and Y/N 

SELECT Distinct(SoldAsVacant), Count(SoldAsVacant)
FROM PortfolioProject..NashvilleHousingDatabase
GROUP BY SoldAsVacant
ORDER BY 2

-- Changing to Yes and No since theres more of them (less computation)


SELECT SoldAsVacant,
CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
	WHEN SoldAsVacant = 'N' THEN 'No'
	ELSE SoldAsVacant
	END
FROM PortfolioProject..NashvilleHousingDatabase


UPDATE NashvilleHousingDatabase
SET SoldAsVacant = CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
	WHEN SoldAsVacant = 'N' THEN 'No'
	ELSE SoldAsVacant
	END

-- Remove Duplicates
--WITH RowNumCTE AS (
SELECT *, 
	ROW_NUMBER() OVER(
	PARTITION BY ParcelID, PropertyAddress, SalePrice, SaleDate, LegalReference
	ORDER BY UniqueID) as row_num

FROM PortfolioProject..NashvilleHousingDatabase
ORDER BY ParcelID

WITH RowNumCTE AS (
SELECT *, 
	ROW_NUMBER() OVER(
	PARTITION BY ParcelID, PropertyAddress, SalePrice, SaleDate, LegalReference
	ORDER BY UniqueID) as row_num

FROM PortfolioProject..NashvilleHousingDatabase
)

SELECT *
FROM RowNumCTE
WHERE row_num > 1
ORDER BY PropertyAddress

-- No Duplicates!


SELECT *
FROM PortfolioProject..NashvilleHousingDatabase

ALTER TABLE PortfolioProject..NashvilleHousingDatabase
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress

ALTER TABLE PortfolioProject..NashvilleHousingDatabase
DROP COLUMN SaleDate

