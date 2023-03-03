// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/SaveGame.h"
#include "CharacterSaveState.generated.h"

/**
 * 
 */
UCLASS()
class TUNICREDRESSED_API UCharacterSaveState : public USaveGame
{
	GENERATED_BODY()

public:
	UPROPERTY(Editanywhere)
		FTransform playerTransform;

	UPROPERTY(Editanywhere)
		UPROPERTY(Editanywhere)
		UPROPERTY(Editanywhere)
		UPROPERTY(Editanywhere)
		UPROPERTY(Editanywhere)
		UPROPERTY(Editanywhere)
		UPROPERTY(Editanywhere)
};
